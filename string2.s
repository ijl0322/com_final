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
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
jne IF_ELSE_else_0
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_0
IF_ELSE_else_0:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_0:
leaq L_.str4(%rip), %rcx
pushq %rcx
leaq L_.str5(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
jne IF_ELSE_else_1
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_1
IF_ELSE_else_1:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_1:
pushq -24(%rbp)
pushq -16(%rbp)
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
jne IF_ELSE_else_2
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_2
IF_ELSE_else_2:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_2:
pushq -24(%rbp)
leaq L_.str6(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -8(%rbp)
leaq L_.str7(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
jne IF_ELSE_else_3
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_3
IF_ELSE_else_3:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_3:
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -8(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -8(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
jne IF_ELSE_else_4
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_4
IF_ELSE_else_4:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_4:
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
je IF_ELSE_else_5
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_5
IF_ELSE_else_5:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_5:
leaq L_.str8(%rip), %rcx
pushq %rcx
leaq L_.str9(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
je IF_ELSE_else_6
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_6
IF_ELSE_else_6:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_6:
pushq -24(%rbp)
pushq -16(%rbp)
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
je IF_ELSE_else_7
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_7
IF_ELSE_else_7:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_7:
pushq -24(%rbp)
leaq L_.str10(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -8(%rbp)
leaq L_.str11(%rip), %rcx
pushq %rcx
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
je IF_ELSE_else_8
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_8
IF_ELSE_else_8:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_8:
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -8(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -16(%rbp)
pushq -24(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
pushq -8(%rbp)
popq %rsi
popq %rdi
callq _cat
pushq %rax
popq %rsi
popq %rdi
callq _strcmp
pushq %rax
popq %rax
cmpq $0, %rax
je IF_ELSE_else_9
pushq $1
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_9
IF_ELSE_else_9:
pushq $0
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_9:
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
.asciz "hello"
L_.str2:
.asciz "helll"
L_.str3:
.asciz "hellp"
L_.str4:
.asciz "abc"
L_.str5:
.asciz "abc"
L_.str6:
.asciz "abc"
L_.str7:
.asciz "ab"
L_.str8:
.asciz "abc"
L_.str9:
.asciz "abc"
L_.str10:
.asciz "abc"
L_.str11:
.asciz "ab"
