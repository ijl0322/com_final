import parser_cstr
from print_tree import print_tree
from functools import partial

symbol_table = [{"scope": "global", "var_count": 0, "var": {}}]                  #ex. {"scope": , "var_count": , "var": {"a": {"type": "int", "addr": 0}}} 
assembly = []
strings = []
str_count = 0
compare_op = {"==": "jne", "!=": "je", ">=": "jl", "<=": "jg", ">": "jle", "<": "jge"}
jump_count = 0
cat_called = False
is_function_scope = True
is_not_function_scope = False

def check_type(tree, key):
    return tree[0] in key
    
is_int_const = partial(check_type, key = ["CONST_INT"])
is_str_const = partial(check_type, key = ["CONST_STRING"])    
is_func_def = partial(check_type, key = ["DEF_FUNC"])   
is_var_dec = partial(check_type, key = ["DEC_VAR"])   
is_id = partial(check_type, key = ["IDENT"])
is_comp_state = partial(check_type, key = ["COMP_STATE"])
is_state = partial(check_type, key = ["STATE"])
is_ret = partial(check_type, key = ["RETURN"])
is_assign = partial(check_type, key = ["ASSIGN"])
is_func_call = partial(check_type, key = ["CALL_FUNC"])
is_expr_additive = partial(check_type, key = ["PLUS", "MINUS"])
is_expr_multiplicative = partial(check_type, key = ["MUL", "DIV", "MODULO"])
is_expr_state = partial(check_type, key = ["PLUS", "MINUS", "DIV", "MUL", "MODULO", "PRIME_EXPR", "NEG", "CALL_FUNC", "CONST_INT", "CONST_STRING"])
is_prime_expr = partial(check_type, key = ["PRIME_EXPR"])
is_neg_expr = partial(check_type, key = ["NEG"])
is_shift_expr = partial(check_type, key = ["SHIFTLEFT", "SHIFTRIGHT"])
is_if = partial(check_type, key = ["IF"])
is_if_else = partial(check_type, key = ["ELSE"])
is_select_state = partial(check_type, key = ["IF","ELSE"])
is_for = partial(check_type, key = ["FOR"])
is_while = partial(check_type, key = ["WHILE"])
is_do_while = partial(check_type, key = ["DO_WHILE"])
is_iter_state = partial(check_type, key = ["DO_WHILE", "FOR", "WHILE"])




def add_code(string):
    assembly.append(string)


def assem_func_declare(name):
    add_code(".globl _%s" %(name))
    add_code("_%s:" %(name))    
    add_code("pushq %rbp")
    add_code("movq %rsp, %rbp")
    add_code("subq $256, %rsp")
    
def assem_ret():
    add_code("popq %rax")
    add_code("leave")
    add_code("retq")
    
def assem_condition(cond):
    comp, expr1, expr2 = cond
    trav_expr(expr1)
    trav_expr(expr2)
    add_code("popq %rbx")     #expr2
    add_code("popq %rax")     #expr1
    add_code("cmpq %rbx, %rax")
    return compare_op[comp]
    
def assem_str(str_count, str_const):
    add_code("leaq L_.str%d(%%rip), %%rcx" %str_count)
    strings.append("L_.str%d:" %str_count)
    strings.append(".asciz %s" %str_const)

def assem_func_call(expression):
    (_, name, param) = expression
    if name == "printd":
        if len(param) != 1: 
            raise ValueError("Incorrect number of parameters for function printd")
        trav_expr(param[0])
        add_code("popq %rax")
        add_code("movq %rax, %rdi")        ## the result should be already in rax. need to fix this if its not!!
        add_code("callq _printd")
        
    elif name == "printf":
        if len(param) != 1:
            raise ValueError("Incorrect number of parameters for function printd")
        print param
        trav_expr(param[0])
        add_code("popq %rdi")
        add_code("movl %eax, %esi")
        add_code("movb $0, %al")
        add_code("callq _printf")
        
    elif name == "sleep":
        if len(param) != 1:
            raise ValueError("Incorrect number of parameters for function sleep")
        trav_expr(param[0])
        add_code("popq %rdi")
        add_code("callq _sleep")
        
    elif name == "cat":
        if len(param) != 2:
            raise ValueError("Incorrect number of parameters for function cat")
        global cat_called
        cat_called = True
        trav_expr(param[0])
        trav_expr(param[1])
        add_code("popq %rsi")
        add_code("popq %rdi")
        add_code("callq _cat")     
        add_code("pushq %rax")
        
    elif name == "eq" or name == "ne":
        if len(param) != 2:
            raise ValueError("Incorrect number of parameters for function eg")        
        trav_expr(param[0])
        trav_expr(param[1])
        add_code("popq %rsi")
        add_code("popq %rdi")
        add_code("callq _strcmp")
        add_code("pushq %rax")
        
    elif name == "put_char_at" or name == "get_char_at":
        pass
        
    else:
        for i in range(len(param)):
            trav_expr(param[i])
            add_code("popq %%r%s" %(8+i))   ##mac uses r9, r10, r11... to store parameters
            add_code("call _%s" %(name))
            add_code("pushq %rax")
        
        
def assem_math_op(op):
    add_code("popq %rbx")
    add_code("popq %rax")
    add_code("cqto")
    add_code("%s %%rbx, %%rax" %(op))
    add_code("pushq %rax")     
        
        
def assem_cat():
    add_code(".globl _cat")
    add_code("_cat: ")
    add_code("pushq %rbp")
    add_code("movq %rsp, %rbp")
    add_code("subq $48, %rsp")
    add_code("movl $256, %eax")
    add_code("movl %eax, %ecx")
    add_code("movq %rdi, -8(%rbp)")
    add_code("movq %rsi, -16(%rbp)")
    add_code("movq %rcx, %rdi")
    add_code("callq _malloc")
    add_code("movq $-1, %rdx")
    add_code("movq %rax, -24(%rbp)")
    add_code("movq -24(%rbp), %rdi")
    add_code("movq -8(%rbp), %rsi")
    add_code("callq ___strcpy_chk")
    add_code("movq $-1, %rdx")
    add_code("movq -24(%rbp), %rdi")
    add_code("movq -16(%rbp), %rsi")
    add_code("movq %rax, -32(%rbp) ")
    add_code("callq ___strcat_chk")
    add_code("movq -24(%rbp), %rcx")
    add_code("movq %rax, -40(%rbp)")
    add_code("movq %rcx, %rax")
    add_code("addq $48, %rsp")
    add_code("popq %rbp")
    add_code("retq")

def trav_tree(tree):
    if is_func_def(tree):
        _,t,d,comp = tree  #_,type, declarator, compound statement
        trav_func_declarator(d)
        trav_comp(comp)
        pop_scope()
        
        
        
def trav_func_declarator(tree):
     n, p = tree # func_id, parameter list
     add_scope(n, is_function_scope)
     assem_func_declare(n)
     if p:
        for param in p:
            add_var(param)
            var_info = find_var(param[1])
            #print var_info
            #print symbol_table
            add_code("movq %%r%s, %s(%%rbp)" %((var_info["addr"] + 7), get_addr(param[1])))
         
def trav_comp(comp):
    ## Can have declaration list, instruction list both, or none
    _, lst = comp     
    declaration = []
    state = []
    for i in lst:
        if is_var_dec(i):
            declaration.append(i)
        elif is_state(i):
            state.append(i) 
    trav_declaration_list(declaration)
    trav_state_list(state)
    #print declaration
    #print state
     
def trav_declaration_list(dlist):
    ## declaration list is a list of declarators, go thru each one using map
    map(trav_var_declarator, dlist)
    
def trav_var_declarator(d):
    ## variables declared, add to symbol table
    _, t, var_list = d
    for (_, var) in var_list:
        add_var((t,var))
    
def trav_state_list(slist):
    map(trav_state, slist)
    
def trav_state(s):
    #print s
    if is_assign(s[1]):
        #print s[1]
        _, var, val = s[1]    ##need to check type
        var_info = find_var(var)
        #print var, val
        if var_info["type"] == "int" and  val[0] == "CONST_INT":
            add_code("movq $%s, %d(%%rbp)" %(str(val[1]), get_addr(var)))
        elif var_info["type"] == "string" and  val[0] == "CONST_STRING":
            global str_count
            str_count += 1
            assem_str(str_count, val[1])
            add_code("movq %%rcx, %d(%%rbp)" %(get_addr(var)))
            
        elif is_expr_state(val):
            trav_expr(val)        #finish calculating the value of the expression first, then assign it to variable
            add_code("popq %rax")
            add_code("movq %%rax, %d(%%rbp)" %(get_addr(var)))            
        else:
            raise ValueError("Variable %s is of type %s, cannot assign value %s" %(var, val[0], str(val)))
            
    elif is_ret(s[1]):
        _, e = s[1]    #RET, expression
        trav_expr(e)
        assem_ret()
        
    
    elif is_expr_state(s[1]):
        trav_expr(s[1])
        
    elif is_select_state(s[1]):
        trav_select_state(s[1])
    elif is_comp_state(s[1]):
        trav_comp(s[1])
        
    elif is_iter_state(s[1]):
        trav_iter_state(s[1])
                
def trav_expr(e):
    if is_id(e):
        _, var = e
        add_code("pushq %d(%%rbp)" %(get_addr(var)))
        
    elif is_int_const(e):
        _, n = e
        add_code("pushq $%s" %(n))   
        
        
    elif is_expr_additive(e) and is_valid_str_op(e):
        op, x, y = e
        if op == "PLUS":
            alternative_state = ('CALL_FUNC', 'cat', [x, y])
            assem_func_call(alternative_state)
        else:
            raise ValueError("%s is not a valid operation for strings" %op)
            
        
    elif is_expr_additive(e):
        op, x, y = e
        trav_expr(x)
        trav_expr(y)
        if op == "PLUS":
            assem_math_op("addq")
        else:
            assem_math_op("subq")
    elif is_expr_multiplicative(e):
        op, x, y = e
        trav_expr(x)
        trav_expr(y)
        if op == "MUL":
            assem_math_op("imulq")
        else:
            assem_math_op("idivq")
        if op == "MODULO":
            add_code("popq %rax")
            add_code("movq %rdx, %rax")
            add_code("pushq %rax")
    elif is_prime_expr(e):
        _, expr = e
        trav_expr(expr)
            
    elif is_neg_expr(e):
        _, expr = e
        trav_expr(expr)
        add_code("popq %rax")
        add_code("negq %rax")
        add_code("pushq %rax")
        
    elif is_shift_expr(e):
        op, x, y = e
        trav_expr(x)
        trav_expr(y)
        add_code("popq %rcx")
        add_code("popq %rax")
        add_code("cltd") 
        if op == "SHIFTLEFT":        
            add_code("shll %cl, %eax")
        else:
            add_code("shrl %cl, %eax")
        add_code("pushq %rax")
    
    elif is_func_call(e):
        assem_func_call(e)    
    
    elif is_str_const(e):
        global str_count
        global has_string
        has_string = True
        _, str_const = e
        str_count += 1
        add_code("leaq L_.str%d(%%rip), %%rcx" %str_count)
        add_code("pushq %rcx")
        strings.append("L_.str%d:" %str_count)
        strings.append(".asciz %s" %str_const)

        
def trav_select_state(s):
    global jump_count
    
    
    if is_if(s) and s[1][0] == "CALL_FUNC":  ##eq and ne

        comp_op = "jne" if s[1][1] == "eq" else "je"        
        _, cond, state = s
        loop_tag = jump_count
        assem_func_call(s[1])
        add_code("popq %rax") 
        add_code("cmpq $0, %rax")
        add_code("%s IF_end%d" %(comp_op, loop_tag))
        add_scope("IF_%d" %(loop_tag), is_not_function_scope)
        trav_state(state)
        add_code("IF_end%d:" %(loop_tag))
        pop_scope()
        jump_count += 1   
    
    elif is_if_else(s) and s[1][0] == "CALL_FUNC":  
        comp_op = "jne" if s[1][1] == "eq" else "je"        
        _, cond, state1, state2 = s
        loop_tag = jump_count
        
        
        assem_func_call(s[1])
        add_code("popq %rax") 
        add_code("cmpq $0, %rax")
        add_code("%s IF_ELSE_else_%d" %(comp_op, loop_tag))
        
        add_scope("IF_ELSE_if%d" %(loop_tag), is_not_function_scope)
        trav_state(state1)
        add_code("jmp IF_ELSE_end_%d" %(loop_tag))
        pop_scope()
        
        add_code("IF_ELSE_else_%d:" %(loop_tag))
        add_scope("IF_ELSE_else%d" %(loop_tag), is_not_function_scope)
        trav_state(state2)
        add_code("IF_ELSE_end_%d:" %(loop_tag))
        pop_scope()
        jump_count += 1
        
    elif is_if(s) and is_valid_str_op(s):
        _, (comp, expr1, expr2), state = s
        op = "eq" if comp == "==" else "ne"
        alternative_state = ('IF', ('CALL_FUNC', op, [expr1, expr2]))        
        trav_select_state(alternative_state)
    
    elif is_if_else(s) and is_valid_str_op(s):
        _, (comp, expr1, expr2), state1, state2 = s
        op = "eq" if comp == "==" else "ne"
        alternative_state = ('ELSE', ('CALL_FUNC', op, [expr1, expr2]))        
        trav_select_state(alternative_state)
        
    
    elif is_if(s):
        #print s
        loop_tag = jump_count
        _, (comp, expr1, expr2), state = s
        #print "=======" ,state
        trav_expr(expr1)
        trav_expr(expr2)
        
        add_code("popq %rbx")     #expr2
        add_code("popq %rax")     #expr1
        add_code("cmpq %rbx, %rax")
        add_code("%s IF_end%d" %(compare_op[comp], loop_tag))
        add_scope("IF_%d" %(loop_tag), is_not_function_scope)
        trav_state(state)
        add_code("IF_end%d:" %(loop_tag))
        pop_scope()
        jump_count += 1
        
    elif is_if_else(s):
        #print s
        loop_tag = jump_count
        _, (comp, expr1, expr2), state1, state2 = s
        #print state1
        #print state2
        trav_expr(expr1)
        trav_expr(expr2)
        add_code("popq %rbx")     #expr2
        add_code("popq %rax")     #expr1
        add_code("cmpq %rbx, %rax")
        add_code("%s IF_ELSE_else_%d" %(compare_op[comp], loop_tag))
        
        add_scope("IF_ELSE_if%d" %(loop_tag), is_not_function_scope)
        trav_state(state1)
        add_code("jmp IF_ELSE_end_%d" %(loop_tag))
        pop_scope()
        
        add_code("IF_ELSE_else_%d:" %(loop_tag))
        add_scope("IF_ELSE_else%d" %(loop_tag), is_not_function_scope)
        trav_state(state2)
        add_code("IF_ELSE_end_%d:" %(loop_tag))
        pop_scope()
        jump_count += 1
        
        
        
def trav_iter_state(s):
    global jump_count
    loop_tag = jump_count
    if is_for(s):        
        jump_count += 1
        _, init, cond, action, state = s

        add_scope("FOR_%d" %(loop_tag), is_not_function_scope)
        trav_state(("STATE", init))     ##initial value
        add_code("FOR_start_%d:" %(loop_tag))
        compare_op = assem_condition(cond)   ##compare
        add_code("%s FOR_end_%d" %(compare_op, loop_tag))       ##jump to end if loop should not be executed
        trav_state(state)                    ##else execute loop
        trav_state(("State", action))    ##increment/ decrement
        
        add_code("jmp FOR_start_%d" %(loop_tag))   ##jump back to start
        add_code("FOR_end_%d:" %(loop_tag))  ##end of for loop 
        
        
    elif is_while(s):
        jump_count += 1
        _, cond, state = s
        add_scope("WHILE_%d" %(loop_tag), is_not_function_scope)
        add_code("WHILE_start_%d:" %(loop_tag))
        compare_op = assem_condition(cond)
        add_code("%s WHILE_end_%d" %(compare_op, loop_tag))
        trav_state(state)    
        add_code("jmp WHILE_start_%d" %(loop_tag))
        add_code("WHILE_end_%d:" %(loop_tag))
        
        
    elif is_do_while(s):
        jump_count += 1
        _, state, cond = s
        add_scope("DO_WHILE_%d" %(loop_tag), is_not_function_scope)
        #print state
        #print cond
        add_code("DO_WHILE_start_%d:" %(loop_tag))
        trav_state(state)
        compare_op = assem_condition(cond)
        add_code("%s DO_WHILE_end_%d" %(compare_op, loop_tag))
        add_code("jmp DO_WHILE_start_%d" %(loop_tag))
        add_code("DO_WHILE_end_%d:" %(loop_tag))
        

def add_scope(name, is_func_scope):
    if is_func_scope == True:
        symbol_table.append({"scope": name, "var_count": 0, "var": {}})
    else:
        var_count = symbol_table[-1]["var_count"] 
        symbol_table.append({"scope": name, "var_count": var_count, "var": {}})
        
def pop_scope():
    symbol_table.pop()
    
def add_var((t,v)):
    table = symbol_table[-1]
    if v in table["var"]:
        raise ValueError("Duplicate variable definition for variable %s" %(v))
    addr_offset = table["var_count"] + 1
    table["var_count"] += 1
    table["var"][v] = {"type": t, "addr": addr_offset}

def get_addr(var):
    var_info = find_var(var)
    return -8 * (var_info["addr"])
        
def find_var(var):
    for table in symbol_table[::-1]:
        #print table
        if var in table["var"]:
            return table["var"][var] 
    raise ValueError("Varaible '%s' has not been defined" %(var))     
    
def is_str_op(t):
    ## check if the given subtree contains const string or variables that are strings
    flag = False
    if type(t) == tuple and t[0] == "IDENT":
        var_info = find_var(t[1])
        if var_info["type"] == "string":
            return True
    elif t[0] == "STATE":
        return False
    elif type(t) == list or type(t) == tuple and t[0]:      
        for item in t:
            if is_str_op(item):
                flag = True
        return flag
    else:
        return t == "CONST_STRING"

def is_int_op(t):
    ## check if the given subtree contains const int or variables that are int
    flag = False
    if type(t) == tuple and t[0] == "IDENT":
        var_info = find_var(t[1])
        if var_info["type"] == "int":
            return True
    elif t[0] == "STATE":
        return False
    elif type(t) == list or type(t) == tuple:      
        for item in t:
            if is_int_op(item):
                flag = True
        return flag
    else:
        return t == "CONST_INT"
        
def is_valid_str_op(t):   
    ## make sure we're not trying to perform operation on different types
    if is_str_op(t) and is_int_op(t):
        raise ValueError("Cannot perform operation on different types")
    elif is_str_op(t) and not is_int_op(t):
        return True
    return False
       
                      
if __name__ == '__main__':
    
    
    #S = raw_input()
    #S = 'int main(){int a; int b; a = -5; b = 0; return a;}' OK
    #S = 'int main(){int a; int b; a = -5; b = 0; printd((-a+7)*-5); return a;}' 
    #S = 'int main(){int a; int b; a = (5+3)*2+1; printd(a); return a;}' OK
    #S = 'int main() {int a; int b; a = 2; b = 2; printd(a>>b); printd(a<<b); return 0;}'
    #S = 'int foo(int a, int b){return a + b;} int main() {int c; int d; c = -5; d = 0; printd(foo(c, d)); return 0;}'
    #S = "int main() {int k; k = 5; if (k > 0) {printd(998);}}" #ok
    #S = "int main() {int k; k = 5; if (k != 5) {int i; i = 998; printd(i);} else {int j; j = 512; printd(j);}}"
    #S = "int main() {int i; for(i=0;i<10;i=i+1){printd(i);} for(i=0;i<10;i=i+1){printd(i);} return 0;}"
    #S = "int main() {int i; i = 0; while(i<10){i=i+1; printd(i);} return 0;}" #WHIle loop ok
    #S = "int main() {int i; for(i=0; i<10; i = i+1){sleep(1); printd(i);} return 0;}"
    #####################################
    S = 'int main() {string i; string k; i = "hi"; k = "hello"; printf(i+k); return 0;}'
    #S = 'int main() {string i; string k; i = "hi"; k = "hi"; if(eq(i, k)){printd(9882);} else {printd(8876);} return 0;}'
    #S = 'int main() {string s; string t; string u; s = "hello"; t = "helll"; u = "hellp"; if (eq(s,t)) printd(1); else printd(0); return 0;}'
    #S = 'int main() {string k; string i; string j; k = "he"; i = "hello"; j = "llo"; if(ne(cat(k,j),i)){printd(9998);} return 0;}'
    #S = 'int main() {string k; string i; k="hello"; i="world"; printf(k+i); return 0;}'
    #S = raw_input("Input expression: ")
    #S = "int main() {int i; i = 3 - 5; i = 3 + 5; i = 3 * 5; i = 3 / 5; i = 3 % 5;}" #Arithmetic operations ok
    #S = "int main() {int i; if(i>0){printf(i);}}"  #If statement ok

    #S = "int main() {int i; i = 1; do{i=i+1; printd(i);} while(i<10); return 0;}" #Do While loop ok
    #S = "extern int foo2(int x, int y);int main() {int i; string k; if (i < 0) {int j; i = i + 1;}}" #Extern function ok
    #S = "extern int foo2(int x, int y);"
    #S = "int main() {int i; if (i < 0) {i = i + 1;}}" #If statement ok

    #S = 'int main(){int a, b, i; string k; a=5; b=10; k = "hi"; for(i=0;i<10;i=i+1){k = "no";}}'


    #source = sys.argv[-1]
    S = open("registers/test/stringCPP.c", "r").read()
    parser = parser_cstr.myparser
    ast = parser.parse(S)
    print ast
    print_tree(ast, 1)
    map(trav_tree, ast)
    print symbol_table
    if cat_called:
        assem_cat()
    print '\n'.join(assembly)
    print '\n'.join(strings)

    
    

