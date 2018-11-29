'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        param = consdecl.param 
        local = param + consdecl.local
        e = SubBody(frame,glenv)
        for x in local:
            e = self.visit(x,e)
        body = consdecl.body

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        stmt = list(map(lambda x: self.visit(x, e), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitVarDecl(self, ast, o):
        ctxt = o
        name = ast.variable.name
        mtype = ast.varType
        if not ctxt.frame:
            self.emit.printout(self.emit.emitATTRIBUTE(name, mtype, None, None))
            return SubBody(None, [Symbol(ast.variable.name,ast.varType, CName(self.className))] + ctxt.sym)
        else:
            self.emit.printout(self.emit.emitVAR(ctxt.frame.getNewIndex(), name, mtype, ctxt.frame.getStartLabel(), ctxt.frame.getEndLabel(), ctxt.frame))
            return SubBody(ctxt.frame, [Symbol(ast.variable.name,ast.varType,ctxt.frame.getCurrIndex()-1)] + ctxt.sym)

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitAssign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym 
        rhs_code, rhs_type = self.visit(ast.exp, Access(frame, env, False, True))
        lhs_code, lhs_type = self.visit(ast.lhs, Access(frame, env, True, True))
        result = rhs_code + lhs_code
        self.emit.printout(result)

    def visitIf(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        env = ctxt.sym
        result = ""
        expr, mtype = self.visit(ast.expr, Access(frame, env, False, False))
        result.append(expr)
        falseLabel = frame.getNewLabel()
        endLabel = frame.getNewLabel()
        result.append(self.emit.emitIFFALSE(falseLabel, frame))
        thenStmt = list(map(lambda x: self.visit(x,SubBody(frame,env)), ast.thenStmt))
        result.append(self.emit.emitGOTO(endLabel, frame))
        result.append(self.emit.emitLABEL(falseLabel, frame))
        elseStmt = list(map(lambda x: self.visit(x,SubBody(frame,env)), ast.elseStmt))
        result.append(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(result)

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        valL, typL = self.visit(ast.left, o)
        valR, typR = self.visit(ast.right, o) 
        if type(typL) is FloatType or type(typR) is FloatType:
            mtype = FloatType()
            if type(typL) is IntType:
                valL = valL + self.emit.emitI2F(frame)
            elif type(typR) is IntType:
                valR = valR + self.emit.emitI2F(frame)
        elif ast.op == '/':
            mtype = FloatType()
        elif ast.op.lower() in ["<","<=",">",">=","<>","=","and","andthen","or","orelse"]:
            mtype = BoolType()
        else: 
            mtype = IntType()
        if ast.op == "+" or ast.op == "-":
            op = self.emit.emitADDOP(ast.op, mtype, frame)
        elif ast.op =="*" or ast.op == "/":
            op = self.emit.emitMULOP(ast.op, mtype, frame)
        elif ast.op.lower() == "div":
            op = self.emit.emitDIV(frame)
        elif ast.op.lower() == "mod":
            op = self.emit.emitMOD(frame)
        elif ast.op.lower() == "and":
            op = self.emit.emitANDOP(frame)
        elif ast.op.lower() == "or":
            op = self.emit.emitOROP(frame)
        else:
            op = self.emit.emitREOP(ast.op, mtype, frame)
        result = valL + valR + op 
        return result, mtype

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        codeOp, typeOp = self.visit(ast.body, o)
        if type(typeOp) is IntType or FloatType:
            result = codeOp + self.emit.emitNEGOP(typeOp, frame)
            return result, typeOp
        else:
            result = codeOp + self.emit.emitNOT(typeOp, frame)
            return result, BoolType()

    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        res = in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        return res, sym.mtype.rettype

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        res = self.lookup(ast.name.lower(), o.sym, lambda x: x.name)
        if o.isLeft:
            if type(res.value) is CName:
                return self.emit.emitPUTSTATIC("MPClass/"+res.name, res.mtype, frame), res.mtype
            else: 
                return self.emit.emitWRITEVAR(res.name, res.mtype, res.value, frame), res.mtype
        else:
            if type(res.value) is CName:
                return self.emit.emitGETSTATIC('MPClass/'+res.name, res.mtype, frame), res.mtype
            else:
                return self.emit.emitREADVAR(res.name, res.mtype, res.value, frame), res.mtype

    def visitArrayCell(self, ast, o):
        ctxt = o
        frame = ctxt.frame

    def visitIntLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        ctxt = o 
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    
