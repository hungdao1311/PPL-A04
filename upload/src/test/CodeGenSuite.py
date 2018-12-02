import unittest
from TestUtils import TestCodeGen
from StaticCheck import *
from CodeGenerator import *
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast1(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putFloat"),[FloatLiteral(10.2)])])])
    	expect = "10.2"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_op2(self):
        input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))])])])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,502))
        
    def test_mulop3(self):
        input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[BinaryOp("*",IntLiteral(5),IntLiteral(3))])])])
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    
    def test_i2f4(self):
        input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putFloat"),[BinaryOp("*",IntLiteral(5),FloatLiteral(3.0))])])])
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_vardecl5(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putFloat"),[BinaryOp("*",IntLiteral(5),FloatLiteral(3.0))])])])
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))
        
    def test_vardecl6(self):
        varlist = [VarDecl(Id("a"),IntType()), VarDecl(Id("b"),FloatType())]
        input = Program(varlist)
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_assign7(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(5)),
    			CallStmt(Id("putFloat"),[BinaryOp("*",Id("a"),FloatLiteral(3.0))])])])
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_assign8(self):
        input = Program([VarDecl(Id("a"),IntType()), 
                        VarDecl(Id("b"),FloatType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(5)),
                Assign(Id("b"),FloatLiteral(5.0)),
    			CallStmt(Id("putFloat"),[BinaryOp("*",Id("a"),Id("b"))])])])
        expect = "25.0"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_assign9(self):
        input = Program([
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),FloatType()),
                FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[
                    Assign(Id('a'),IntLiteral(2)),
                    CallStmt(Id("putInt"),[Id('a')])])])

        expect  = "2"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    
    def test_if10(self):
        input = Program([VarDecl(Id(r'a'),IntType()),
                        FuncDecl(Id(r'main'),[],[],[
                            If(BinaryOp(r'<',IntLiteral(3),IntLiteral(5)),[Assign(Id(r'a'),IntLiteral(3))],[Assign(Id(r'a'),IntLiteral(2))]),
                            CallStmt(Id(r'putInt'),[Id(r'a')])])])
        expect  = "3"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_param11(self):    
    	input = Program([VarDecl(Id(r'a'),IntType()),
                FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[VarDecl(Id(r'f'),FloatType())],[Assign(Id(r'f'),FloatLiteral(5.0)),CallStmt(Id(r'putFloatLn'),[Id(r'f')]),Return(IntLiteral(1))],IntType()),
                FuncDecl(Id(r'main'),[],[VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(2)),CallStmt(Id(r'foo'),[Id(r'a')]),CallStmt(Id(r'putInt'),[Id(r'a')])],VoidType())])
    	expect = "5.0\n2"
    	self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_random12(self):
        input = Program([FuncDecl(Id("main"),[],[],[CallStmt(Id("putFloat"),[BinaryOp("+",BinaryOp("/",BinaryOp("-",IntLiteral(8),IntLiteral(2)),IntLiteral(3)),BinaryOp("*",BinaryOp("/",IntLiteral(9),IntLiteral(3)),BinaryOp("/",IntLiteral(6),IntLiteral(2))))]),Return(None)])])
        expect = "11.0"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_random13(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("count"),IntType()),VarDecl(Id("max"),IntType()),VarDecl(Id("check"),IntType())],[Assign(Id("count"),IntLiteral(1)),Assign(Id("max"),IntLiteral(5)),Assign(Id("check"),IntLiteral(1)),While(BinaryOp("and",BinaryOp("<",Id("count"),Id("max")),BinaryOp("<",Id("check"),IntLiteral(10))),[CallStmt(Id("putInt"),[Id("count")]),While(BinaryOp("<",Id("check"),IntLiteral(5)),[CallStmt(Id("putInt"),[Id("check")]),Assign(Id("check"),BinaryOp("+",Id("check"),IntLiteral(1))),While(BinaryOp("<",Id("count"),IntLiteral(3)),[Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])]),Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))),Assign(Id("check"),BinaryOp("+",Id("check"),IntLiteral(1)))]),Return(None)])])
        expect = "112344"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_while14(self):
        input = Program([VarDecl(Id(r'a'),IntType()),
                        FuncDecl(Id(r'main'),[],[],[
                            Assign(Id("a"),IntLiteral(3)),
                            While(BinaryOp(r'<',Id("a"),IntLiteral(5)),[Assign(Id(r'a'),BinaryOp("+",Id("a"),IntLiteral(1)))]),
                            CallStmt(Id(r'putInt'),[Id(r'a')])])])
        expect  = "5"
        self.assertTrue(TestCodeGen.test(input,expect,514)) 
    
    def test_random15(self):
        input = Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType()),
                        FuncDecl(Id("foo"),[VarDecl(Id("i"),IntType())],[],[Assign(Id("a"),BinaryOp("+",Id("a"),Id("i"))),Return(BinaryOp(">=",Id("i"),IntLiteral(5)))], BoolType()),
                        FuncDecl(Id("main"),[],[VarDecl(Id("x"),BoolType())],[Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("or",BinaryOp("or",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("orelse",BinaryOp("orelse",BinaryOp("orelse",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(4)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("or",BinaryOp("or",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(3)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putIntLn"),[Id("a")]),Assign(Id("a"),IntLiteral(0)),CallStmt(Id("putBoolLn"),[BinaryOp("orelse",BinaryOp("orelse",BinaryOp("or",CallExpr(Id("foo"),[IntLiteral(1)]),CallExpr(Id("foo"),[IntLiteral(2)])),CallExpr(Id("foo"),[IntLiteral(5)])),CallExpr(Id("foo"),[IntLiteral(7)]))]),CallStmt(Id("putInt"),[Id("a")]),Return(None)])])
        expect = """true
13
false
10
true
13
true
8"""
        self.assertTrue(TestCodeGen.test(input,expect,515))

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
                [Assign(Id("a"),BinaryOp(">",BinaryOp("+",IntLiteral(9),IntLiteral(4)),IntLiteral(20))),If(Id("a"),[With([VarDecl(Id("b"),IntType())],[Assign(Id("b"),IntLiteral(3)),CallStmt(Id("putBoolLn"),[BooleanLiteral(True)]),CallStmt(Id("putIntLn"),[IntLiteral(3)])])],[CallStmt(Id("putBoolLn"),[BooleanLiteral(True)])]),CallStmt(Id("putInt"),[IntLiteral(8)]),Return(None)])])
        expect = """true
8"""
        self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_put19(self):
        input = Program([
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),FloatType()),
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("test19")])])])

        expect  = "test19"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    
    def test_put20(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putBool"),[BooleanLiteral(True)])])])

        expect  = "true"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_put21(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putBool"),[BooleanLiteral(False)])])])

        expect  = "false"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    
    def test_put22(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putFloat"),[FloatLiteral(2.22)])])])

        expect  = "2.22"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_put23(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("aaaabbbbccc2.23")])])])

        expect  = "aaaabbbbccc2.23"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_binop24(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(5)),
    			CallStmt(Id("putInt"),[BinaryOp("div",Id("a"),IntLiteral(3))])])])
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_binop25(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(5)),
    			CallStmt(Id("putInt"),[BinaryOp("mOd",Id("a"),IntLiteral(3))])])])
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_shortcircuit26(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(False)),
    			CallStmt(Id("putBool"),[BinaryOp("andthen",Id("a"),BooleanLiteral(True))])])])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_shortcircuit27(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
    			CallStmt(Id("putBool"),[BinaryOp("orelse",Id("a"),BooleanLiteral(True))])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_unop28(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
    			CallStmt(Id("putBool"),[UnaryOp("not",Id("a"))])])])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_unop29(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(False)),
    			CallStmt(Id("putBoolLn"),[UnaryOp("not",Id("a"))])])])
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    
    def test_unop30(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(6)),
    			CallStmt(Id("putIntLn"),[UnaryOp("-",Id("a"))])])])
        expect = "-6\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    
    def test_unop31(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(6)),
    			CallStmt(Id("putIntLn"),[UnaryOp("-",Id("a"))])])])
        expect = "-6\n"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_unop32(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(22)),
    			CallStmt(Id("putInt"),[UnaryOp("-",Id("a"))])])])
        expect = "-22"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test_binop33(self):
        input = Program([VarDecl(Id("a"),FloatType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),FloatLiteral(8.0)),
    			CallStmt(Id("putFloat"),[BinaryOp("/",Id("a"),IntLiteral(2))])])])
        expect = "4.0"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_binop34(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(2)),
    			CallStmt(Id("putFloat"),[BinaryOp("/",Id("a"),IntLiteral(2))])])])
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test_binop35(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(2)),
    			CallStmt(Id("putBool"),[BinaryOp(">",Id("a"),IntLiteral(2))])])])
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    
    def test_binop36(self):
        input = Program([VarDecl(Id("a"),IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),IntLiteral(2)),
    			CallStmt(Id("putBool"),[BinaryOp(">=",Id("a"),IntLiteral(2))])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    
    def test_binop37(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
    			CallStmt(Id("putBool"),[BinaryOp("and",Id("a"),BooleanLiteral(True))])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_binop38(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
    			CallStmt(Id("putBool"),[BinaryOp("or",Id("a"),BooleanLiteral(False))])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_return39(self):
        input = Program([VarDecl(Id("a"),BoolType()),
            FuncDecl(Id("foo"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
                If(Id("a"),[Return(IntLiteral(4))],[Return(IntLiteral(5))])
            ],IntType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
    			CallStmt(Id("putBool"),[BinaryOp("or",Id("a"),BooleanLiteral(False))])])])
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_binop40(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putBoolLn"),[UnaryOp("not",BinaryOp(">",IntLiteral(2),IntLiteral(2)))]),
                    CallStmt(Id("putIntLn"),[BinaryOp("-",IntLiteral(2),IntLiteral(2))])
                ])
        ])
        expect = 'true\n0\n'
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_if41(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
                If(Id("a"),[CallStmt(Id("putIntLn"),[IntLiteral(3)])],[CallStmt(Id("putBoolLn"),[Id("a")])]),
    			CallStmt(Id("putBool"),[BinaryOp("or",Id("a"),BooleanLiteral(False))])])])
        expect = "3\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_if42(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(False)),
                If(Id("a"),[CallStmt(Id("putIntLn"),[IntLiteral(3)])],[CallStmt(Id("putBoolLn"),[Id("a")])]),
    			CallStmt(Id("putBool"),[BinaryOp("or",Id("a"),BooleanLiteral(True))])])])
        expect = "false\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_put43(self):
        input = Program([
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),FloatType()),
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("ababababababa")])])])

        expect  = "ababababababa"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_string44(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putStringLn"),[StringLiteral("testtt44")])])])

        expect  = "testtt44\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_string45(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putStringLn"),[StringLiteral("testtt45")])])])

        expect  = "\ntesttt45\n"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test_string46(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("hangtren")]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putString"),[StringLiteral("hangduoi")]),
                    ])])

        expect  = "hangtren\nhangduoi"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_string47(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("hangtren")]),
                    CallStmt(Id("putString"),[StringLiteral("hangtren")]),
                    ])])

        expect  = "hangtrenhangtren"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    
    def test_string48(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putStringLn"),[StringLiteral("hangtren")]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putStringLn"),[StringLiteral("hang3")]),
                    ])])

        expect  = "hangtren\n\nhang3\n"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_put49(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putIntLn"),[BinaryOp("-",IntLiteral(9),IntLiteral(2))])
                ])
        ])
        expect = '\n7\n'
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_put50(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putIntLn"),[BinaryOp("-",IntLiteral(9),IntLiteral(2))])
                ])
        ])
        expect = '\n7\n'
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_for_with_if51(self):
        input = Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'a'),IntLiteral(1)),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[With([VarDecl(Id(r'a'),IntType())],[For(Id(r'a'),IntLiteral(2),IntLiteral(3),True,[With([VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'putIntLn'),[Id(r'a')])])])])],[]),With([VarDecl(Id(r'c'),IntType())],[CallStmt(Id(r'putInt'),[Id(r'a')])]),Return(None)],VoidType())])
        expect = "2\n3\n1"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_if52(self):
        input = Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'<',IntLiteral(3),IntLiteral(6)),[Assign(Id(r'a'),IntLiteral(3))],[Assign(Id(r'a'),IntLiteral(2))]),CallStmt(Id(r'putInt'),[Id(r'a')])],VoidType())])
        expect  = "3"
        self.assertTrue(TestCodeGen.test(input,expect,552)) 

    def test_if53(self):
        input = Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[],[If(BinaryOp(r'<',IntLiteral(3),IntLiteral(6)),[Assign(Id(r'a'),IntLiteral(2))],[]),CallStmt(Id(r'putInt'),[Id(r'a')])],VoidType())])
        expect  = "2"
        self.assertTrue(TestCodeGen.test(input,expect,553)) 

    def test_unop55(self):    
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putBoolLn"),[UnaryOp('not',BooleanLiteral(True))]),
                CallStmt(Id("putBool"),[UnaryOp('not',BooleanLiteral(False))])])])
    	expect = "false\ntrue"
    	self.assertTrue(TestCodeGen.test(input,expect,554)) 

    def test_unop56(self):    
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putIntLn"),[UnaryOp('-',IntLiteral(1))]),
                CallStmt(Id("putFloat"),[UnaryOp('-',FloatLiteral(5.0))])])])
    	expect = "-1\n-5.0"
    	self.assertTrue(TestCodeGen.test(input,expect,555)) 

    def test_local56(self):
        input = Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'a'),IntType())],[Assign(Id(r'b'),IntLiteral(10)),If(BinaryOp(r'>',IntLiteral(3),IntLiteral(6)),[Assign(Id(r'b'),IntLiteral(3))],[]),CallStmt(Id(r'putInt'),[Id(r'b')])],VoidType())])
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,556)) 

    def test_local57(self):    
    	input = Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType())],[Assign(Id(r'b'),IntLiteral(2)),If(BinaryOp(r'<',IntLiteral(3),IntLiteral(6)),[Assign(Id(r'b'),IntLiteral(3))],[]),CallStmt(Id(r'putInt'),[Id(r'b')])],VoidType())])
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,557)) 

    def test_param58(self):    
    	input = Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'foo'),[VarDecl(Id(r'a'),IntType())],[VarDecl(Id(r'f'),FloatType())],[Assign(Id(r'f'),FloatLiteral(5.0)),CallStmt(Id(r'putFloatLn'),[Id(r'f')]),Return(IntLiteral(1))],IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(2)),CallStmt(Id(r'foo'),[Id(r'a')]),CallStmt(Id(r'putInt'),[Id(r'a')])],VoidType())])
    	expect = "5.0\n2"
    	self.assertTrue(TestCodeGen.test(input,expect,558)) 

    def test_while59(self):    
    	input = Program([VarDecl(Id(r'a'),IntType()),FuncDecl(Id(r'main'),[],[VarDecl(Id(r'b'),IntType())],[Assign(Id(r'a'),IntLiteral(3)),Assign(Id(r'b'),IntLiteral(2)),While(BinaryOp(r'>',Id(r'a'),Id(r'b')),[Assign(Id(r'a'),IntLiteral(5)),Assign(Id(r'b'),IntLiteral(5))]),CallStmt(Id(r'putInt'),[Id(r'a')])],VoidType())])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,559)) 

    def test_binop60(self):    
    	input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("+",BinaryOp("-",IntLiteral(10),BinaryOp("*",IntLiteral(9),IntLiteral(8))),BinaryOp("DIV",IntLiteral(6),IntLiteral(4)))),CallStmt(Id("putInt"),[Id("a")]),Return(None)],VoidType())])
    	expect = "-61"
    	self.assertTrue(TestCodeGen.test(input,expect,560)) 

    def test_put61(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putFloat"),[FloatLiteral(102.2)])])])
    	expect = "102.2"
    	self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_shortcircuit62(self):    
     	input =Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType())],[Assign(Id(r'a'),BinaryOp(r'orelse',BinaryOp(r'orelse',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(True))),Assign(Id(r'b'),BinaryOp(r'orelse',BinaryOp(r'orelse',BooleanLiteral(False),BooleanLiteral(False)),BooleanLiteral(False))),CallStmt(Id(r'putBoolLn'),[Id(r'a')]),CallStmt(Id(r'putBool'),[Id(r'b')]),Return(None)],VoidType())])
     	expect = "true\nfalse"
     	self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_shortcircuit63(self):    
     	input = Program([FuncDecl(Id(r'main'),[],[VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType())],[Assign(Id(r'a'),BinaryOp(r'andthen',BinaryOp(r'andthen',BooleanLiteral(True),BooleanLiteral(True)),BooleanLiteral(True))),Assign(Id(r'b'),BinaryOp(r'andthen',BinaryOp(r'andthen',BooleanLiteral(True),BooleanLiteral(False)),BooleanLiteral(True))),CallStmt(Id(r'putBoolLn'),[Id(r'a')]),CallStmt(Id(r'putBool'),[Id(r'b')]),Return(None)],VoidType())])
     	expect = "true\nfalse"
     	self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_put64(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putFloat"),[FloatLiteral(12.2)])])])
    	expect = "12.2"
    	self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_binop65(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putBoolLn"),[UnaryOp("not",BinaryOp(">",IntLiteral(2),IntLiteral(2)))]),
                    CallStmt(Id("putIntLn"),[BinaryOp("-",IntLiteral(5),IntLiteral(2))])
                ])
        ])
        expect = 'true\n3\n'
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_if66(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
                If(Id("a"),[CallStmt(Id("putIntLn"),[IntLiteral(3)])],[CallStmt(Id("putIntLn"),[IntLiteral(4)])]),
    			CallStmt(Id("putBool"),[BinaryOp("and",Id("a"),BooleanLiteral(False))])])])
        expect = "3\nfalse"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_if67(self):
        input = Program([VarDecl(Id("a"),BoolType()),
    		FuncDecl(Id("main"),[],[],[
                Assign(Id("a"),BooleanLiteral(True)),
                If(Id("a"),[CallStmt(Id("putIntLn"),[IntLiteral(7)])],[CallStmt(Id("putBoolLn"),[Id("a")])]),
    			CallStmt(Id("putBoolLn"),[BinaryOp("or",Id("a"),BooleanLiteral(True))])])])
        expect = "7\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_put68(self):
        input = Program([
                VarDecl(Id("b"),StringType()),
                VarDecl(Id("c"),IntType()),
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("put68")])])])

        expect  = "put68"
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_string69(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putStringLn"),[StringLiteral("sttttt69")])])])

        expect  = "sttttt69\n"
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_string70(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putStringLn"),[StringLiteral("70707070")])])])

        expect  = "\n70707070\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    
    def test_string71(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("tren")]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putString"),[StringLiteral("duoi")]),
                    ])])

        expect  = "tren\nduoi"
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_string72(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("motmot")]),
                    CallStmt(Id("putString"),[StringLiteral("haihai")]),
                    ])])

        expect  = "motmothaihai"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_string73(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putStringLn"),[StringLiteral("mot")]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putStringLn"),[StringLiteral("ba")]),
                    ])])

        expect  = "mot\n\nba\n"
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_put74(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putFloatLn"),[BinaryOp("/",IntLiteral(9),IntLiteral(2))])
                ])
        ])
        expect = '\n4.5\n'
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_put75(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putIntLn"),[BinaryOp("div",IntLiteral(9),IntLiteral(2))])
                ])
        ])
        expect = '\n4\n'
        self.assertTrue(TestCodeGen.test(input,expect,575))
    
    def test_string76(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putString"),[StringLiteral("motmot")]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putString"),[StringLiteral("haihai")]),
                    ])])

        expect  = "motmot\nhaihai"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_string77(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putStringLn"),[StringLiteral("mot")]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putStringLn"),[StringLiteral("bon")]),
                    ])])

        expect  = "mot\n\n\nbon\n"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_put78(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putIntLn"),[BinaryOp("+",IntLiteral(9),IntLiteral(2))])
                ])
        ])
        expect = '\n11\n'
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_put79(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putLn"),[]),
                    CallStmt(Id("putIntLn"),[BinaryOp("mod",IntLiteral(10),IntLiteral(2))])
                ])
        ])
        expect = '\n0\n'
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_random80(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("+",BinaryOp("-",IntLiteral(2),BinaryOp("*",IntLiteral(5),IntLiteral(8))),BinaryOp("DIV",IntLiteral(20),IntLiteral(4)))),CallStmt(Id("putInt"),[Id("a")]),Return(None)])])
        expect = "-33"
        self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_multi81(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("-",BinaryOp("-",IntLiteral(2),BinaryOp("*",IntLiteral(5),IntLiteral(1))),BinaryOp("moD",IntLiteral(20),IntLiteral(4)))),CallStmt(Id("putInt"),[Id("a")]),Return(None)])])
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_multi82(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("*",BinaryOp("-",IntLiteral(2),BinaryOp("-",IntLiteral(5),IntLiteral(1))),BinaryOp("+",IntLiteral(20),IntLiteral(4)))),CallStmt(Id("putIntLn"),[Id("a")]),Return(None)])])
        expect = "-48\n"
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_multi83(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("*",BinaryOp("+",IntLiteral(2),BinaryOp("+",IntLiteral(3),IntLiteral(1))),BinaryOp("*",IntLiteral(2),IntLiteral(4)))),CallStmt(Id("putIntLn"),[Id("a")]),Return(None)])])
        expect = "48\n"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_multi84(self):
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),BinaryOp("+",BinaryOp("-",IntLiteral(10),BinaryOp("+",IntLiteral(7),IntLiteral(2))),BinaryOp("*",IntLiteral(2),IntLiteral(4)))),CallStmt(Id("putIntLn"),[Id("a")]),Return(None)])])
        expect = "9\n"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_multi85(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[FloatLiteral(1.2)]),
                CallStmt(Id("putLn"),[]),
                CallStmt(Id("putFloat"),[FloatLiteral(1.2)]),
                ])])
        expect = "1.2\n1.2"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    
    def test_put86(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[FloatLiteral(1.2)]),
                CallStmt(Id("putLn"),[]),
                CallStmt(Id("putFloatLn"),[FloatLiteral(1.2)]),
                ])])
        expect = "1.2\n1.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    
    def test_put87(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloatLn"),[FloatLiteral(1.2)]),
                CallStmt(Id("putFloatLn"),[FloatLiteral(2.2)]),
                ])])
        expect = "1.2\n2.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_put88(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putIntLn"),[IntLiteral(2)]),
                CallStmt(Id("putFloatLn"),[FloatLiteral(2.2)]),
                ])])
        expect = "2\n2.2\n"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    
    def test_put89(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putIntLn"),[IntLiteral(8)]),
                CallStmt(Id("putIntLn"),[FloatLiteral(9)]),
                ])])
        expect = "8\n9\n"
        self.assertTrue(TestCodeGen.test(input,expect,589))
    
    def test_put90(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putInt"),[IntLiteral(9)]),
                CallStmt(Id("putLn"),[]),
                CallStmt(Id("putIntLn"),[FloatLiteral(0)]),
                ])])
        expect = "9\n0\n"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_string91(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putInt"),[IntLiteral(9)]),
                CallStmt(Id("putLn"),[]),
                CallStmt(Id("putString"),[StringLiteral("1-test")]),
                ])])
        expect = "9\n1-test"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_string92(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putStringLn"),[StringLiteral("test9")]),
                CallStmt(Id("putString"),[StringLiteral("2")]),
                ])])
        expect = "test9\n2"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    
    def test_string93(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putString"),[StringLiteral("test")]),
                CallStmt(Id("putString"),[StringLiteral("93")]),
                ])])
        expect = "test93"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_put94(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putString"),[StringLiteral("test")]),
                CallStmt(Id("putInt"),[IntLiteral(94)]),
                ])])
        expect = "test94"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_put95(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putStringLn"),[StringLiteral("test")]),
                CallStmt(Id("putIntLn"),[IntLiteral(95)]),
                ])])
        expect = "test\n95\n"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    
    def test_put96(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putStringLn"),[StringLiteral("string ket hop voi int")]),
                CallStmt(Id("putInt"),[IntLiteral(96)]),
                ])])
        expect = "string ket hop voi int\n96"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_random97(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putStringLn"),[StringLiteral("string ket hop voi float")]),
                CallStmt(Id("putFloat"),[FloatLiteral(9.7)]),
                ])])
        expect = "string ket hop voi float\n9.7"
        self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_random98(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putString"),[StringLiteral("string ket hop voi bool ")]),
                CallStmt(Id("putBool"),[BooleanLiteral(True)]),
                ])])
        expect = "string ket hop voi bool true"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    
    def test_random99(self):
        input = Program([FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putString"),[StringLiteral("string ket hop voi bool ")]),
                CallStmt(Id("putBool"),[BooleanLiteral(False)]),
                ])])
        expect = "string ket hop voi bool false"
        self.assertTrue(TestCodeGen.test(input,expect,599))