.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
Label0:
	iconst_1
	ifgt Label3
	iconst_1
	ifle Label2
Label3:
	iconst_1
	goto Label4
Label2:
	iconst_0
Label4:
	ifgt Label6
	iconst_1
	ifle Label5
Label6:
	iconst_1
	goto Label7
Label5:
	iconst_0
Label7:
	istore_1
	iconst_0
	ifgt Label9
	iconst_0
	ifle Label8
Label9:
	iconst_1
	goto Label10
Label8:
	iconst_0
Label10:
	ifgt Label12
	iconst_0
	ifle Label11
Label12:
	iconst_1
	goto Label13
Label11:
	iconst_0
Label13:
	istore_2
	iload_1
	invokestatic io/putBoolLn(Z)V
	iload_2
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 19
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
