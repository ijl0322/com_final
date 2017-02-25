.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
movq $123, -8(%rbp)
pushq -8(%rbp)
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $123
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $123
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq -8(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $0
popq %rax
leave
retq

