.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i1 I from Label0 to Label1
.var 2 is i2 I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpgt Label3
	goto Label5
Label5:
	iconst_1
	istore_2
Label8:
	iload_2
	bipush 10
	if_icmpgt Label7
	goto Label9
Label9:
	iload_2
	invokestatic io/putInt(I)V
	iload_2
	iload_1
	iconst_1
	isub
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	goto Label6
Label12:
	iload_2
	iload_1
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	goto Label7
Label15:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label7:
	iload_1
	iconst_3
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label2
Label18:
	iload_1
	iconst_5
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label21
	goto Label3
Label21:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 11
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
