.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass/a I
	getstatic MPClass/a I
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
.var 1 is a I from Label5 to Label6
Label5:
	iconst_2
	istore_1
Label9:
	iload_1
	iconst_3
	if_icmpgt Label8
	goto Label10
Label10:
.var 2 is b I from Label11 to Label12
Label11:
	iload_1
	invokestatic io/putIntLn(I)V
Label12:
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label9
Label8:
Label6:
Label4:
.var 1 is c I from Label13 to Label14
Label13:
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
Label14:
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
