.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
.var 1 is f F from Label0 to Label1
Label0:
	ldc 5.0
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_2
	putstatic MPClass/a I
	getstatic MPClass/a I
	invokestatic MPClass/foo(I)I
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
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
