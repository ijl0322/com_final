.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
movq $45000, -8(%rbp)
movq $3, -16(%rbp)
pushq -8(%rbp)
pushq -16(%rbp)
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $45000
pushq -16(%rbp)
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq -8(%rbp)
pushq $3
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $45000
pushq $3
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rcx
popq %rax
cltd
shll %cl, %eax
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
pushq -16(%rbp)
popq %rcx
popq %rax
cltd
shll %cl, %eax
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
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rcx
popq %rax
cltd
shll %cl, %eax
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
pushq $3
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $45000
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rcx
popq %rax
cltd
shll %cl, %eax
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $0
popq %rax
leave
retq

