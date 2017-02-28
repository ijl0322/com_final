	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 12
	.globl	_put_char_at
	.align	4, 0x90
_put_char_at:                           ## @put_char_at
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
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	%edx, -16(%rbp)
	movl	-16(%rbp), %edx
	movb	%dl, %al
	movslq	-12(%rbp), %rdi
	movq	-8(%rbp), %rcx
	movb	%al, (%rcx,%rdi)
	movl	-16(%rbp), %eax
	popq	%rbp
	retq
	.cfi_endproc

	.globl	_call_put_char
_call_put_char:                         ## @call_put_char
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$32, %rsp
	movl	$128, %eax
	movl	%eax, %ecx
	movq	%rdi, -8(%rbp)
	movq	%rcx, %rdi
	callq	_malloc
	movq	$-1, %rdx
	movq	%rax, -16(%rbp)
	movq	-16(%rbp), %rdi
	movq	-8(%rbp), %rsi
	callq	___strcpy_chk
	movl	$2, %esi
	movl	$98, %edx
	movq	-16(%rbp), %rdi
	movq	%rax, -24(%rbp)         ## 8-byte Spill
	callq	_put_char_at
	movq	-16(%rbp), %rcx
	movl	%eax, -28(%rbp)         ## 4-byte Spill
	movq	%rcx, %rax
	addq	$32, %rsp
	popq	%rbp
	retq


	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp6:
	.cfi_def_cfa_offset 16
Ltmp7:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp8:
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	leaq	L_.str(%rip), %rax
	movl	$0, -4(%rbp)
	movq	%rax, -16(%rbp)
	movq	-16(%rbp), %rdi
	callq	_call_put_char
	leaq	L_.str.1(%rip), %rdi
	movq	%rax, -16(%rbp)
	movq	-16(%rbp), %rsi
	movb	$0, %al
	callq	_printf
	xorl	%ecx, %ecx
	movl	%eax, -20(%rbp)         ## 4-byte Spill
	movl	%ecx, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"bello"

L_.str.1:                               ## @.str.1
	.asciz	"%s\n"


.subsections_via_symbols
