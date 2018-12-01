.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 8
	iconst_2
	isub
	i2f
	iconst_3
	i2f
	fdiv
	bipush 9
	i2f
	iconst_3
	i2f
	fdiv
	bipush 6
	i2f
	iconst_2
	i2f
	fdiv
	fmul
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
.limit locals 1
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
