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
_call_get_char:
pushq %rbp
movq %rsp, %rbp
subq $16, %rsp
movq %rax, -8(%rbp)
movq -8(%rbp), %rdi
callq _get_char_at
addq $16, %rsp
popq %rbp
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

