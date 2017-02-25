.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
movq $45000, -8(%rbp)
pushq $123
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, -16(%rbp)
movq $43, -24(%rbp)
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -24(%rbp)
popq %rbx
popq %rax
cqto
imulq %rbx, %rax
pushq %rax
pushq $100
popq %rbx
popq %rax
cqto
idivq %rbx, %rax
pushq %rax
pushq -16(%rbp)
pushq -24(%rbp)
popq %rbx
popq %rax
cqto
imulq %rbx, %rax
pushq %rax
pushq -8(%rbp)
popq %rbx
popq %rax
cqto
idivq %rbx, %rax
pushq %rax
popq %rax
movq %rdx, %rax
pushq %rax
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cqto
subq %rbx, %rax
pushq %rax
pushq -24(%rbp)
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
pushq -24(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cqto
subq %rbx, %rax
pushq %rax
pushq $2
popq %rcx
popq %rax
cltd
shrl %cl, %eax
pushq %rax
popq %rbx
popq %rax
cqto
idivq %rbx, %rax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $0
popq %rax
leave
retq

