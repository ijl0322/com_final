import parser_cstr
from print_tree import print_tree
from functools import partial

virtual_stack = []
symbol_table = [{"scope": "global", "var_count": 0, "var": {}}]                  #ex. {"scope": , "var_count": , "var": {"a": {"type": "int", "addr": 0}}} 
assembly = []
compare_op = {"==": "jne", "!=": "je", ">=": "jl", "<=": "jg", ">": "jle", "<": "jge"}
jump_count = 0
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
    ##add_code("popq %rax")
    add_code("movq %s, %%rax" %(virtual_stack.pop()))
    add_code("leave")
    add_code("retq")
    
def assem_condition(cond):
    comp, expr1, expr2 = cond
    trav_expr(expr1)
    trav_expr(expr2)
    ##add_code("popq %rbx")     #expr2
    ##add_code("popq %rax")     #expr1
    add_code("movq %s, %%rbx" %(virtual_stack.pop()))
    add_code("movq %s, %%rax" %(virtual_stack.pop()))
    add_code("cmpq %rbx, %rax")
    return compare_op[comp]
    
    
def assem_func_call(expression):
    (_, name, param) = expression
    if name == "printd":
        if len(param) != 1: 
            raise ValueError("Incorrect number of parameters for function printd")
        trav_expr(param[0])
        #add_code("popq %rax")
        add_code("movq %s, %%rax" %(virtual_stack.pop()))
        add_code("movq %rax, %rdi")        ## the result should be already in rax. need to fix this if its not!!
        add_code("callq _printd")
    else:
        for i in range(len(param)):
            trav_expr(param[i])
            ##add_code("popq %%r%s" %(8+i))   ##mac uses r9, r10, r11... to store parameters
            add_code("movq %s, %%r%s" %(virtual_stack.pop(), 8+i))
        add_code("movq %s, %%rax" %(virtual_stack.pop()))
        add_code("call _%s" %(name))
        ####add_code("pushq %rax")
        virtual_stack.append("%rax")
        
def assem_math_op(op):
    ##add_code("popq %rbx")
    ##add_code("popq %rax")
    add_code("movq %s, %%rbx" %(virtual_stack.pop()))
    add_code("movq %s, %%rax" %(virtual_stack.pop()))
    add_code("cqto")
    add_code("%s %%rbx, %%rax" %(op))
    add_code("movq %rax, %r10")
    ###add_code("pushq %rax")    
    virtual_stack.append("%r10") 
        
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
            ## TODO 
            ## add string handling
            pass
            
        elif is_expr_state(val):
            trav_expr(val)        #finish calculating the value of the expression first, then assign it to variable
            ##add_code("popq %rax")
            add_code("movq %s, %%rax" %(virtual_stack.pop()))
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
        print "if"
        trav_select_state(s[1])
    elif is_comp_state(s[1]):
        trav_comp(s[1])
        
    elif is_iter_state(s[1]):
        trav_iter_state(s[1])
                
def trav_expr(e):
    if is_id(e):
        _, var = e
        ###add_code("pushq %d(%%rbp)" %(get_addr(var)))
        virtual_stack.append("%d(%%rbp)" %(get_addr(var)))
        
    elif is_int_const(e):
        _, n = e
        ####add_code("pushq $%s" %(n)) 
        virtual_stack.append("$%s" %(n))
        
    elif is_expr_additive(e):
        op, x, y = e

        print x[0], y[0]
        if x[0] == "PRIME_EXPR" and y[0] == "PRIME_EXPR":
            trav_expr(x)
            add_code("movq %s, %%r9" %(virtual_stack.pop()))
            virtual_stack.append("%r9")
            trav_expr(y)
        else:
            trav_expr(x)
            trav_expr(y)
            
        if op == "PLUS":
            assem_math_op("addq")
        else:
            assem_math_op("subq")
    elif is_expr_multiplicative(e):
        op, x, y = e
        if x[0] == "PRIME_EXPR" and y[0] == "PRIME_EXPR":
            trav_expr(x)
            add_code("movq %s, %%r9" %(virtual_stack.pop()))
            virtual_stack.append("%r9")
            trav_expr(y)
        else:
            trav_expr(x)
            trav_expr(y)
        if op == "MUL":
            assem_math_op("imulq")
        else:
            assem_math_op("idivq")
        if op == "MODULO":
            ##add_code("popq %rax")
            add_code("movq %s, %%rax" %(virtual_stack.pop()))
            add_code("movq %rdx, %rax")
            ### add_code("pushq %rax")
            virtual_stack.append("%rax")
    elif is_prime_expr(e):
        _, expr = e
        trav_expr(expr)
            
    elif is_neg_expr(e):
        _, expr = e
        trav_expr(expr)
        ##add_code("popq %rax")
        add_code("movq %s, %%rax" %(virtual_stack.pop()))
        add_code("negq %rax")
        ### add_code("pushq %rax")
        virtual_stack.append("%rax")
        
    elif is_shift_expr(e):
        op, x, y = e
        if x[0] == "PRIME_EXPR" and y[0] == "PRIME_EXPR":
            trav_expr(x)
            add_code("movq %s, %%r9" %(virtual_stack.pop()))
            virtual_stack.append("%r9")
            trav_expr(y)
        else:
            trav_expr(x)
            trav_expr(y)
        ##add_code("popq %rcx")
        ##add_code("popq %rax")
        add_code("movq %s, %%rcx" %(virtual_stack.pop()))
        add_code("movq %s, %%rax" %(virtual_stack.pop()))        
        
        add_code("cltd") 
        if op == "SHIFTLEFT":        
            add_code("shll %cl, %eax")
        else:
            add_code("shrl %cl, %eax")
        ###add_code("pushq %rax")
        virtual_stack.append("%rax")
    
    elif is_func_call(e):
        assem_func_call(e)    

def trav_select_state(s):
    global jump_count
    
    if is_if(s):
        print s
        loop_tag = jump_count
        _, (comp, expr1, expr2), state = s
        print "=======" ,state
        trav_expr(expr1)
        trav_expr(expr2)
        
        ###add_code("popq %rbx")     #expr2
        ###add_code("popq %rax")     #expr1
        add_code("movq %s, %%rbx" %(virtual_stack.pop()))
        add_code("movq %s, %%rax" %(virtual_stack.pop()))
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
        ##add_code("popq %rbx")     #expr2
        ##add_code("popq %rax")     #expr1
        add_code("movq %s, %%rbx" %(virtual_stack.pop()))
        add_code("movq %s, %%rax" %(virtual_stack.pop()))       
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
        _, init, cond, action, state = s
        #print init
        #print cond
        #print action
        #print state
        add_scope("FOR_%d" %(loop_tag), is_not_function_scope)
        trav_state(("STATE", init))     ##initial value
        add_code("FOR_start_%d:" %(loop_tag))
        compare_op = assem_condition(cond)   ##compare
        add_code("%s FOR_end_%d" %(compare_op, loop_tag))       ##jump to end if loop should not be executed
        trav_state(state)                    ##else execute loop
        trav_state(("State", action))    ##increment/ decrement
        
        add_code("jmp FOR_start_%d" %(loop_tag))   ##jump back to start
        add_code("FOR_end_%d:" %(loop_tag))  ##end of for loop 
        jump_count += 1
        
    elif is_while(s):
        _, cond, state = s
        add_scope("WHILE_%d" %(loop_tag), is_not_function_scope)
        add_code("WHILE_start_%d:" %(loop_tag))
        compare_op = assem_condition(cond)
        add_code("%s WHILE_end_%d" %(compare_op, loop_tag))
        trav_state(state)    
        add_code("jmp WHILE_start_%d" %(loop_tag))
        add_code("WHILE_end_%d:" %(loop_tag))
        jump_count += 1
        
    elif is_do_while(s):
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
        jump_count += 1

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
      
if __name__ == '__main__':
    
    
    #S = raw_input()
    #S = 'int main(){int a; int b; a = -5; b = 0; return a;}' 
    #S = 'int main(){int a; int b; a = -5; b = 0; printd(a);printd(-a+7);printd((-a+7)*5); return a;}' 
    #S = 'int main(){int a; int b; a = (5+3)*2+1; printd(a); return a;}' 
    #S = 'int main() {int a; int b; a = 2; b = 2; printd(a>>b); printd(a<<b); return 0;}'
    #S = 'int main() {int i; int j; i = 45000; j = -123; printd((i+0) + (j+0)); return 0;}'
    #S = 'int foo(int a, int b){return a + b;} int main() {int c; int d; c = -5; d = 0; printd(foo(c, d)); return 0;}'
    #S = "int main() {int k; k = 5; if (k > 0) {printd(998);}}" #ok
    #S = "int main() {int k; k = 5; if (k != 5) {int i; i = 998; printd(i);} else {int j; j = 512; printd(j);}}"
    #S = "int main() {int i; for(i=0;i<10;i=i+1){printd(i);} for(i=0;i<10;i=i+1){printd(i);} return 0;}"
    #S = "int main() {int i; i = 0; while(i<10){i=i+1; printd(i);} return 0;}" #WHIle loop ok
    #####################################
    #S = raw_input("Input expression: ")
    #S = "int main() {int i; i = 3 - 5; i = 3 + 5; i = 3 * 5; i = 3 / 5; i = 3 % 5;}" #Arithmetic operations ok
    #S = "int main() {int i; if(i>0){printf(i);}}"  #If statement ok

    #S = "int main() {int i; i = 1; do{i=i+1; printd(i);} while(i<10); return 0;}" #Do While loop ok
    #S = "extern int foo2(int x, int y);int main() {int i; string k; if (i < 0) {int j; i = i + 1;}}" #Extern function ok
    #S = "extern int foo2(int x, int y);"
    #S = "int main() {int i; if (i < 0) {i = i + 1;}}" #If statement ok

    #S = 'int main(){int a, b, i; string k; a=5; b=10; k = "hi"; for(i=0;i<10;i=i+1){k = "no";}}'


    #source = sys.argv[-1]
    S = open("test/mod.c", "r").read()
    parser = parser_cstr.myparser
    ast = parser.parse(S)
    print ast
    print_tree(ast, 1)
    map(trav_tree, ast)
    print symbol_table
    print '\n'.join(assembly)

    
    

