.globl _fact
_fact:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
movq %r8, -8(%rbp)
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_end0
pushq $1
popq %rax
leave
retq
IF_end0:
pushq -8(%rbp)
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
subq %rbx, %rax
pushq %rax
popq %r8
call _fact
pushq %rax
popq %rbx
popq %rax
cqto
imulq %rbx, %rax
pushq %rax
popq %rax
leave
retq
.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
pushq $10
popq %r8
call _fact
pushq %rax
popq %rax
movq %rax, %rdi
callq _printd
pushq $0
popq %rax
leave
retq

