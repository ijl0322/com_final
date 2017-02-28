.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
leaq L_.str1(%rip), %rcx
movq %rcx, -8(%rbp)
movq $1, -16(%rbp)
FOR_start_0:
pushq -16(%rbp)
pushq $100
popq %rbx
popq %rax
cmpq %rbx, %rax
jge FOR_end_0
pushq -8(%rbp)
leaq L_.str2(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rax
movq %rax, -8(%rbp)
pushq -16(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -16(%rbp)
jmp FOR_start_0
FOR_end_0:
movq $2, -16(%rbp)
FOR_start_1:
pushq -16(%rbp)
pushq $10
popq %rbx
popq %rax
cmpq %rbx, %rax
jge FOR_end_1
pushq -16(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -24(%rbp)
FOR_start_2:
pushq -24(%rbp)
pushq $100
popq %rbx
popq %rax
cmpq %rbx, %rax
jge FOR_end_2
pushq -8(%rbp)
popq %rdi
movl $48, %edx
movl -24(%rbp), %esi
callq _call_put_char
pushq %rax
popq -8(%rbp)
pushq -24(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -24(%rbp)
jmp FOR_start_2
FOR_end_2:
pushq -16(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -16(%rbp)
jmp FOR_start_1
FOR_end_1:
movq $0, -16(%rbp)
FOR_start_3:
pushq -16(%rbp)
pushq $100
popq %rbx
popq %rax
cmpq %rbx, %rax
jge FOR_end_3
pushq -8(%rbp)
pushq -16(%rbp)
popq %rsi
popq %rax
callq	_call_get_char
pushq %rax
pushq $49
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_end4
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
leaq L_.str5(%rip), %rcx
pushq %rcx
popq %rdi
movl %eax, %esi
movb $0, %al
callq _printf
IF_end4:
pushq -16(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rax
movq %rax, -16(%rbp)
jmp FOR_start_3
FOR_end_3:
leaq L_.str6(%rip), %rcx
pushq %rcx
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
L_.str1:
.asciz "0"
L_.str2:
.asciz "1"
L_.str3:
.asciz "0"
L_.str4:
.asciz "1"
L_.str5:
.asciz " "
L_.str6:
.asciz "\n"
