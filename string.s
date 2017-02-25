.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
leaq L_.str1(%rip), %rcx
movq %rcx, -16(%rbp)
leaq L_.str2(%rip), %rcx
movq %rcx, -24(%rbp)
leaq L_.str3(%rip), %rcx
movq %rcx, -8(%rbp)
leaq L_.str4(%rip), %rcx
pushq %rcx
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
leaq L_.str5(%rip), %rcx
pushq %rcx
leaq L_.str6(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq -16(%rbp)
leaq L_.str7(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
leaq L_.str8(%rip), %rcx
pushq %rcx
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq -16(%rbp)
pushq -8(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq -16(%rbp)
pushq -8(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq -16(%rbp)
pushq -16(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -24(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq -16(%rbp)
pushq -8(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq $0
popq %rax
leave
retq
.globl _cat
_cat: 
pushq %rbp
movq %rsp, %rbp
subq $48, %rsp
movl $256, %eax
movl %eax, %ecx
movq %rdi, -8(%rbp)
movq %rsi, -16(%rbp)
movq %rcx, %rdi
callq _malloc
movq $-1, %rdx
movq %rax, -24(%rbp)
movq -24(%rbp), %rdi
movq -8(%rbp), %rsi
callq ___strcpy_chk
movq $-1, %rdx
movq -24(%rbp), %rdi
movq -16(%rbp), %rsi
movq %rax, -32(%rbp) 
callq ___strcat_chk
movq -24(%rbp), %rcx
movq %rax, -40(%rbp)
movq %rcx, %rax
addq $48, %rsp
popq %rbp
retq
L_.str1:
.asciz "hello"
L_.str2:
.asciz " world\n"
L_.str3:
.asciz "bye"
L_.str4:
.asciz "hello"
L_.str5:
.asciz "hello"
L_.str6:
.asciz "world\n"
L_.str7:
.asciz "world\n"
L_.str8:
.asciz "hello"
