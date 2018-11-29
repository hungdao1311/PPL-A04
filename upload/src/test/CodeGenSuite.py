import unittest
from TestUtils import TestCodeGen
from StaticCheck import *
from CodeGenerator import *
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin putInt(100); end"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[FloatLiteral(10.2)])])])
    # 	expect = "10.2"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_op(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))])])])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
        
    # def test_mulop(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[BinaryOp("*",IntLiteral(5),IntLiteral(3))])])])
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    
    # def test_i2f(self):
    #     input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp("*",IntLiteral(5),FloatLiteral(3.0))])])])
    #     expect = "15.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

    # def test_vardecl(self):
    #     input = Program([VarDecl(Id("a"),IntType()),
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putFloat"),[BinaryOp("*",IntLiteral(5),FloatLiteral(3.0))])])])
    #     expect = "15.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
        
    # def test_vardecl2(self):
    #     varlist = [VarDecl(Id("a"),IntType()), VarDecl(Id("b"),FloatType())]
    #     input = Program(varlist)
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,506))
    
    # def test_assign(self):
    #     input = Program([VarDecl(Id("a"),IntType()),
    # 		FuncDecl(Id("main"),[],[],[
    #             Assign(Id("a"),IntLiteral(5)),
    # 			CallStmt(Id("putFloat"),[BinaryOp("*",Id("a"),FloatLiteral(3.0))])])])
    #     expect = "15.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))
    # def test_assign(self):
    #     input = Program([VarDecl(Id("a"),IntType()), 
    #                     VarDecl(Id("b"),FloatType()),
    # 		FuncDecl(Id("main"),[],[],[
    #             Assign(Id("a"),IntLiteral(5)),
    #             Assign(Id("b"),FloatLiteral(5.0)),
    # 			CallStmt(Id("putFloat"),[BinaryOp("*",Id("a"),Id("b"))])])])
    #     expect = "25.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_assign_glo21(self):
        input = Program([
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),FloatType()),
                FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[
                    Assign(Id('a'),IntLiteral(2)),
                    CallStmt(Id("putInt"),[Id('a')])])])

        expect  = "2"
        self.assertTrue(TestCodeGen.test(input,expect,509))

