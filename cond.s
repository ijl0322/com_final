.globl _main
_main:
pushq %rbp
movq %rsp, %rbp
subq $256, %rsp
movq $450, -8(%rbp)
pushq $123
popq %rax
negq %rax
pushq %rax
popq %rax
movq %rax, -16(%rbp)
pushq -8(%rbp)
pushq $1
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
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_0
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_0
IF_ELSE_else_0:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_0:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_1
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_1
IF_ELSE_else_1:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_1:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_2
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_2
IF_ELSE_else_2:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_2:
pushq $45
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_3
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_3
IF_ELSE_else_3:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_3:
pushq $45
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_4
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_4
IF_ELSE_else_4:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_4:
pushq $45
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_5
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_5
IF_ELSE_else_5:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_5:
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_6
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_6
IF_ELSE_else_6:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_6:
pushq -8(%rbp)
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_7
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_7
IF_ELSE_else_7:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_7:
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jge IF_ELSE_else_8
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_8
IF_ELSE_else_8:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_8:
pushq -8(%rbp)
pushq $1
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
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_9
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_9
IF_ELSE_else_9:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_9:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_10
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_10
IF_ELSE_else_10:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_10:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_11
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_11
IF_ELSE_else_11:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_11:
pushq $45
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_12
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_12
IF_ELSE_else_12:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_12:
pushq $45
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_13
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_13
IF_ELSE_else_13:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_13:
pushq $45
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_14
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_14
IF_ELSE_else_14:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_14:
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_15
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_15
IF_ELSE_else_15:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_15:
pushq -8(%rbp)
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_16
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_16
IF_ELSE_else_16:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_16:
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jle IF_ELSE_else_17
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_17
IF_ELSE_else_17:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_17:
pushq -8(%rbp)
pushq $1
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
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_18
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_18
IF_ELSE_else_18:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_18:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_19
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_19
IF_ELSE_else_19:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_19:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_20
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_20
IF_ELSE_else_20:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_20:
pushq $45
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_21
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_21
IF_ELSE_else_21:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_21:
pushq $45
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_22
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_22
IF_ELSE_else_22:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_22:
pushq $45
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_23
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_23
IF_ELSE_else_23:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_23:
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_24
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_24
IF_ELSE_else_24:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_24:
pushq -8(%rbp)
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_25
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_25
IF_ELSE_else_25:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_25:
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jl IF_ELSE_else_26
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_26
IF_ELSE_else_26:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_26:
pushq -8(%rbp)
pushq $1
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
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_27
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_27
IF_ELSE_else_27:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_27:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_28
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_28
IF_ELSE_else_28:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_28:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_29
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_29
IF_ELSE_else_29:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_29:
pushq $45
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_30
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_30
IF_ELSE_else_30:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_30:
pushq $45
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_31
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_31
IF_ELSE_else_31:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_31:
pushq $45
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_32
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_32
IF_ELSE_else_32:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_32:
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_33
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_33
IF_ELSE_else_33:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_33:
pushq -8(%rbp)
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_34
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_34
IF_ELSE_else_34:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_34:
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jg IF_ELSE_else_35
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_35
IF_ELSE_else_35:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_35:
pushq -8(%rbp)
pushq $1
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
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_36
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_36
IF_ELSE_else_36:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_36:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_37
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_37
IF_ELSE_else_37:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_37:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_38
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_38
IF_ELSE_else_38:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_38:
pushq $45
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_39
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_39
IF_ELSE_else_39:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_39:
pushq $45
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_40
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_40
IF_ELSE_else_40:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_40:
pushq $45
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_41
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_41
IF_ELSE_else_41:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_41:
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_42
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_42
IF_ELSE_else_42:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_42:
pushq -8(%rbp)
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_43
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_43
IF_ELSE_else_43:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_43:
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
jne IF_ELSE_else_44
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_44
IF_ELSE_else_44:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_44:
pushq -8(%rbp)
pushq $1
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
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_45
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_45
IF_ELSE_else_45:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_45:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_46
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_46
IF_ELSE_else_46:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_46:
pushq -8(%rbp)
pushq $1
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_47
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_47
IF_ELSE_else_47:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_47:
pushq $45
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_48
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_48
IF_ELSE_else_48:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_48:
pushq $45
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_49
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_49
IF_ELSE_else_49:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_49:
pushq $45
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_50
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_50
IF_ELSE_else_50:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_50:
pushq -8(%rbp)
pushq -16(%rbp)
pushq $0
popq %rbx
popq %rax
cqto
addq %rbx, %rax
pushq %rax
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_51
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_51
IF_ELSE_else_51:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_51:
pushq -8(%rbp)
pushq $123
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_52
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_52
IF_ELSE_else_52:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_52:
pushq -8(%rbp)
pushq -16(%rbp)
popq %rbx
popq %rax
cmpq %rbx, %rax
je IF_ELSE_else_53
pushq -8(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
jmp IF_ELSE_end_53
IF_ELSE_else_53:
pushq -16(%rbp)
popq %rax
movq %rax, %rdi
callq _printd
IF_ELSE_end_53:
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

