.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
leaq L_.str1(%rip), %rcx
movq %rcx, -8(%rbp)
leaq L_.str2(%rip), %rcx
movq %rcx, -16(%rbp)
pushq -8(%rbp)
pushq -16(%rbp)
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $0
popq %rax
leave
retq
L_.str1:
.asciz "hello"
L_.str2:
.asciz "hello"
