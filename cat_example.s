	.globl	_cat

_cat:                                   ## @cat
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp0:
	.cfi_def_cfa_offset 16
Ltmp1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp2:
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movl	$256, %eax              ## imm = 0x100
	movl	%eax, %ecx
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rcx, %rdi
	callq	_malloc
	movq	$-1, %rdx
	movq	%rax, -24(%rbp)
	movq	-24(%rbp), %rdi
	movq	-8(%rbp), %rsi
	callq	___strcpy_chk
	movq	$-1, %rdx
	movq	-24(%rbp), %rdi
	movq	-16(%rbp), %rsi
	movq	%rax, -32(%rbp)         ## 8-byte Spill
	callq	___strcat_chk
	movq	-24(%rbp), %rcx
	movq	%rax, -40(%rbp)         ## 8-byte Spill
	movq	%rcx, %rax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc

.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
leaq L_.str1(%rip), %rcx
movq %rcx, -8(%rbp)
leaq L_.str2(%rip), %rcx
movq %rcx, -16(%rbp)
movq -8(%rbp), %rdi           ##first string
movq -16(%rbp), %rsi          ##second string
callq	_cat
leaq	L_.str3(%rip), %rdi
movq	%rax, %rsi           ##new memory allocated for first string + second string
movb	$0, %al              ##the address is stored in %rax
callq	_printf
leave
retq



L_.str1:
.asciz "hello "
L_.str2:
.asciz "world\n"
L_.str3:                               ## @.str.2
	.asciz	"%s"
