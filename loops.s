.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
movq $0, -8(%rbp)
WHILE_start_0:
pushq -8(%rbp)
pushq $10
popq %rbx
popq %rax
cmpq %rbx, %rax
jge WHILE_end_0
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
pushq -8(%rbp)
pushq $2
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -8(%rbp)
jmp WHILE_start_0
WHILE_end_0:
pushq $10
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, -8(%rbp)
FOR_start_1:
pushq -8(%rbp)
pushq $10
popq %rbx
popq %rax
cmpq %rbx, %rax
jg FOR_end_1
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -8(%rbp)
jmp FOR_start_1
FOR_end_1:
movq $0, -8(%rbp)
DO_WHILE_start_2:
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
subq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -8(%rbp)
pushq -8(%rbp)
pushq $20
popq %rax
negq %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jl DO_WHILE_end_2
jmp DO_WHILE_start_2
DO_WHILE_end_2:
pushq $0
popq %rax
leave
retq

