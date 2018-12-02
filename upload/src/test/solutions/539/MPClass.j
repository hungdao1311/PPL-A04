.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a Z

.method public static foo()I
Label0:
	iconst_1
	putstatic MPClass/a Z
	getstatic MPClass/a Z
	ifle Label2
	iconst_4
	ireturn
	goto Label3
Label2:
	iconst_5
	ireturn
Label3:
	return
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass/a Z
	getstatic MPClass/a Z
	iconst_0
	ior
	invokestatic io/putBool(Z)V
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
