.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
Label0:
	bipush 9
	iconst_4
	iadd
	bipush 20
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_1
	iload_1
	ifle Label4
.var 2 is b I from Label6 to Label7
Label6:
	iconst_3
	istore_2
	iconst_1
	invokestatic io/putBoolLn(Z)V
	iconst_3
	invokestatic io/putIntLn(I)V
Label7:
	goto Label5
Label4:
	iconst_1
	invokestatic io/putBoolLn(Z)V
Label5:
	bipush 8
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
