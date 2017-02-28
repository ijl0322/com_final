.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
leaq L_.str1(%rip), %rcx
movq %rcx, -8(%rbp)
pushq -8(%rbp)
popq %rdi
movl $97, %edx
movl $0, %esi
callq _call_put_char
pushq %rax
popq -8(%rbp)
pushq -8(%rbp)
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
pushq $0
popq %rax
leave
retq
.globl _call_put_char
_call_put_char:
pushq %rbp
movq %rsp, %rbp
subq $48, %rsp
movl $128, %eax
movl %eax, %ecx
movq %rdi, -8(%rbp)
movl %esi, -12(%rbp)
movl %edx, -16(%rbp)
movq %rcx, %rdi
callq _malloc
movq $-1, %rdx
movq %rax, -24(%rbp)
movq -24(%rbp), %rdi
movq -8(%rbp), %rsi
callq ___strcpy_chk
movq -24(%rbp), %rdi
movl -12(%rbp), %esi
movl -16(%rbp), %edx
movq %rax, -32(%rbp)
callq _put_char_at
movq -24(%rbp), %rcx
movl %eax, -40(%rbp) 
movq %rcx, %rax
addq $48, %rsp
popq %rbp
retq
L_.str1:
.asciz "hello"
