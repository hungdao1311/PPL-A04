import unittest
from TestUtils import TestCodeGen
from StaticCheck import *
from CodeGenerator import *
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
#     def test_int(self):
#         """Simple program: int main() {} """
#         input = """procedure main(); begin putInt(100); end"""
#         expect = "100"
#         self.assertTrue(TestCodeGen.test(input,expect,500))
#     def test_int_ast1(self):
#     	input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putFloat"),[FloatLiteral(10.2)])])])
#     	expect = "10.2"
#     	self.assertTrue(TestCodeGen.test(input,expect,501))
#     def test_op2(self):
#         input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putInt"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))])])])
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,502))
        
#     def test_mulop3(self):
#         input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putInt"),[BinaryOp("*",IntLiteral(5),IntLiteral(3))])])])
#         expect = "15"
#         self.assertTrue(TestCodeGen.test(input,expect,503))
    
#     def test_i2f4(self):
#         input = Program([
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putFloat"),[BinaryOp("*",IntLiteral(5),FloatLiteral(3.0))])])])
#         expect = "15.0"
#         self.assertTrue(TestCodeGen.test(input,expect,504))

#     def test_vardecl5(self):
#         input = Program([VarDecl(Id("a"),IntType()),
#     		FuncDecl(Id("main"),[],[],[
#     			CallStmt(Id("putFloat"),[BinaryOp("*",IntLiteral(5),FloatLiteral(3.0))])])])
#         expect = "15.0"
#         self.assertTrue(TestCodeGen.test(input,expect,505))
        
#     def test_vardecl6(self):
#         varlist = [VarDecl(Id("a"),IntType()), VarDecl(Id("b"),FloatType())]
#         input = Program(varlist)
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,506))
    
#     def test_assign7(self):
#         input = Program([VarDecl(Id("a"),IntType()),
#     		FuncDecl(Id("main"),[],[],[
#                 Assign(Id("a"),IntLiteral(5)),
#     			CallStmt(Id("putFloat"),[BinaryOp("*",Id("a"),FloatLiteral(3.0))])])])
#         expect = "15.0"
#         self.assertTrue(TestCodeGen.test(input,expect,507))

#     def test_assign8(self):
#         input = Program([VarDecl(Id("a"),IntType()), 
#                         VarDecl(Id("b"),FloatType()),
#     		FuncDecl(Id("main"),[],[],[
#                 Assign(Id("a"),IntLiteral(5)),
#                 Assign(Id("b"),FloatLiteral(5.0)),
#     			CallStmt(Id("putFloat"),[BinaryOp("*",Id("a"),Id("b"))])])])
#         expect = "25.0"
#         self.assertTrue(TestCodeGen.test(input,expect,508))
    
#     def test_assign9(self):
#         input = Program([
#                 VarDecl(Id("b"),IntType()),
#                 VarDecl(Id("c"),FloatType()),
#                 FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[
#                     Assign(Id('a'),IntLiteral(2)),
#                     CallStmt(Id("putInt"),[Id('a')])])])

#         expect  = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,509))
    
#     def test_if10(self):
#         input = Program([VarDecl(Id(r'a'),IntType()),
#                         FuncDecl(Id(r'main'),[],[],[
#                             If(BinaryOp(r'<',IntLiteral(3),IntLiteral(5)),[Assign(Id(r'a'),IntLiteral(3))],[Assign(Id(r'a'),IntLiteral(2))]),
#                             CallStmt(Id(r'putInt'),[Id(r'a')])])])
#         expect  = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,510))
    
#     def test_param11(self):    
#     	input = Program([VarDecl(Id(r'a'),IntType()),
#                 FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[VarDecl(Id(r'f'),FloatType())],[Assign(Id(r'f'),FloatLiteral(5.0)),CallStmt(Id(r'putFloatLn'),[Id(r'f')]),Return(IntLiteral(1))],IntType()),
#                 FuncDecl(Id(r'main'),[],[VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(2)),CallStmt(Id(r'foo'),[Id(r'a')]),CallStmt(Id(r'putInt'),[Id(r'a')])],VoidType())])
#     	expect = "5.0\n2"
#     	self.assertTrue(TestCodeGen.test(input,expect,511))

#     def test_random12(self):
#         input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp("+",BinaryOp("/",BinaryOp("-",IntLiteral(8),IntLiteral(2)),IntLiteral(3)),BinaryOp("*",BinaryOp("/",IntLiteral(9),IntLiteral(3)),BinaryOp("/",IntLiteral(6),IntLiteral(2))))]),Return(None)])])
#         expect = "11.0"
#         self.assertTrue(TestCodeGen.test(input,expect,512))

#     def test_random13(self):
#         input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("count"),IntType()),VarDecl(Id("max"),IntType()),VarDecl(Id("check"),IntType())],[Assign(Id("count"),IntLiteral(1)),Assign(Id("max"),IntLiteral(5)),Assign(Id("check"),IntLiteral(1)),While(BinaryOp("and",BinaryOp("<",Id("count"),Id("max")),BinaryOp("<",Id("check"),IntLiteral(10))),[CallStmt(Id("putInt"),[Id("count")]),While(BinaryOp("<",Id("check"),IntLiteral(5)),[CallStmt(Id("putInt"),[Id("check")]),Assign(Id("check"),BinaryOp("+",Id("check"),IntLiteral(1))),While(BinaryOp("<",Id("count"),IntLiteral(3)),[Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])]),Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))),Assign(Id("check"),BinaryOp("+",Id("check"),IntLiteral(1)))]),Return(None)])])
#         expect = "112344"
#         self.assertTrue(TestCodeGen.test(input,expect,513))
    
#     def test_while14(self):
#         input = Program([VarDecl(Id(r'a'),IntType()),
#                         FuncDecl(Id(r'main'),[],[],[
#                             Assign(Id("a"),IntLiteral(3)),
#                             While(BinaryOp(r'<',Id("a"),IntLiteral(5)),[Assign(Id(r'a'),BinaryOp("+",Id("a"),IntLiteral(1)))]),
#                             CallStmt(Id(r'putInt'),[Id(r'a')])])])
#         expect  = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,514)) 
    
#     def test_random15(self):
#         input = Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),
#                         FuncDecl(Id("foo"),[VarDecl(Id("i"),IntType())],[],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("i"))),Return(BinaryOp(">=",Id("i"),IntLiteral(5)))], BoolType()),
#                         FuncDecl(Id("main"),[],[VarDecl(Id("x"),BoolType())],[Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("or",BinaryOp("or",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("orelse",BinaryOp("orelse",BinaryOp("orelse",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(4)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("or",BinaryOp("or",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("orelse",BinaryOp("orelse",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(5)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putInt"),[Id("a")]),Return(None)])])
#         expect = """true
# 13
# false
# 10
# true
# 13
# true
# 8"""
#         self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_16(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("i1"),IntType()),VarDecl(Id("i2"),IntType())],
        [For(Id("i1"),IntLiteral(1),IntLiteral(10),True,
            [For(Id("i2"),IntLiteral(1),IntLiteral(10),True,
                [CallStmt(Id("putInt"),[Id("i2")]),
                    If(BinaryOp('=',Id("i2"),BinaryOp('-',Id("i1"),IntLiteral(1))),
                        [Continue()],[]),
                    If(BinaryOp('=',Id("i2"),Id("i1")),[Break()],[])]),
                        If(BinaryOp('=',Id("i1"),IntLiteral(3)),[Continue()],[]),
                        If(BinaryOp('=',Id("i1"),IntLiteral(5)),[Break()],[])]),Return(None)])])
        expect = "112123123412345"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_for17(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("i1"),IntType()),VarDecl(Id("i2"),IntType())],
        [For(Id("i1"),IntLiteral(2),IntLiteral(1),False,
                    [CallStmt(Id("putInt"),[Id("i1")]),
                    For(Id("i2"),IntLiteral(1),IntLiteral(5),True,
                    [CallStmt(Id("putInt"),[Id("i2")])])])]),Return(None)])
        expect = "212345112345"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_random18(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),BoolType())],
                [Assign(Id("a"),BinaryOp(">",BinaryOp("+",IntLiteral(3),IntLiteral(4)),IntLiteral(5))),If(Id("a"),[With([VarDecl(Id("b"),IntType())],[Assign(Id("b"),IntLiteral(3)),CallStmt(Id("putBoolLn"),[BooleanLiteral(True)]),CallStmt(Id("putIntLn"),[IntLiteral(3)])])],[CallStmt(Id("putBoolLn"),[BooleanLiteral(False)])]),CallStmt(Id("putInt"),[IntLiteral(1)]),Return(None)])])
        expect = """true
3
1"""
        self.assertTrue(TestCodeGen.test(input,expect,518))