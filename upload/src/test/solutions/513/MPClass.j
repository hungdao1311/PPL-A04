.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is count I from Label0 to Label1
.var 2 is max I from Label0 to Label1
.var 3 is check I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_5
	istore_2
	iconst_1
	istore_3
Label2:
	iload_1
	iload_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_3
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ifle Label3
	iload_1
	invokestatic io/putInt(I)V
Label8:
	iload_3
	iconst_5
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
	iload_3
	invokestatic io/putInt(I)V
	iload_3
	iconst_1
	iadd
	istore_3
Label12:
	iload_1
	iconst_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label12
Label13:
	goto Label8
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label1:
	return
.limit stack 10
.limit locals 4
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
