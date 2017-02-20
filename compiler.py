import parser_cstr
from print_tree import print_tree
from functools import partial

symbol_table = []                  #ex. {"scope": , "var_count": , "var": {"a": {"type": "int", "addr": 0}}} 
assembly = []


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
is_expr_state = partial(check_type, key = ["PLUS", "MINUS", "DIV", "MULTI", "MODULO"])

def add_code(string):
    assembly.append(string)


def assem_func_declare(name):
    add_code(".globl _%s" %(name))
    add_code("_%s:" %(name))    
    add_code("pushq %rbp")
    add_code("movq %rsp, %rbp")
    add_code("subq $256, %rsp")
    
def assem_ret():
    add_code("leave")
    add_code("retq")
    
def assem_func_call(expression):
    (_, name, param) = expression
    if name == "printd":
        if len(param) != 1: 
            raise ValueError("Incorrect number of parameters for function printd")
        trav_expr(param[0])
        add_code("popq %rax")
        add_code("movq %rax, %rdi")        ## the result should be already in rax. need to fix this if its not!!
        add_code("callq _printd")
        
def assem_math_op(op):
    add_code("popq %rbx")
    add_code("popq %rax")
    add_code("cltd")
    add_code("%s %%rbx, %%rax" %(op))
    add_code("pushq %rax")     
        
def trav_tree(tree):
    if is_func_def(tree):
        _,t,d,comp = tree  #_,type, declarator, compound statement
        trav_func_declarator(d)
        trav_comp(comp)
        pop_scope()
        assem_ret()
        
        
def trav_func_declarator(tree):
     n, p = tree # func_id, parameter list
     add_scope(n)
     assem_func_declare(n)
     if p:
        for param in p:
            add_var(param)
            var_info = find_var(param[1])
            print var_info
            print symbol_table
            add_code("movq %%r%s, %s(%%rbp)" %((var_info["addr"] + 8), get_addr(param[1])))
         
         ####### need to work on how to add assembly for parameters #####

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
    print declaration
    print state
     
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
    if is_assign(s[1]):
        _, var, (t, val) = s[1]    ##need to check type
        var_info = find_var(var)
        print var, t, val
        if var_info["type"] == "int" and  t == "CONST_INT":
            add_code("movq $%s, %d(%%rbp)" %(str(val), get_addr(var)))
        elif var_info["type"] == "string" and  t == "CONST_STRING":
            ## TODO 
            ## add string handling
            pass
        else:
            raise ValueError("Variable %s is of type %s, cannot assign value %s" %(var, t, str(val)))
            
    elif is_ret(s[1]):
        _, e = s[1]    #RET, expression
        trav_expr(e)
        
    elif is_func_call(s[1]):
        assem_func_call(s[1])
    
    elif is_expr_state(s[1]):
        trav_expr(s[1])
                
def trav_expr(e):
    if is_id(e):
        _, var = e
        add_code("pushq %d(%%rbp)" %(get_addr(var)))
        
    elif is_int_const(e):
        _, n = e
        add_code("pushq $%s" %(n))   
    elif is_expr_additive(e):
        op, x, y = e
        trav_expr(x)
        trav_expr(y)
        if op == "PLUS":
            assem_math_op("addq")
        else:
            assem_math_op("subq")
        
        


    

                           
def add_scope(name):
    symbol_table.append({"scope": name, "var_count": 0, "var": {}})
    
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
    
    #S = 'int main(){int a; int b; a = -5; b = 0; return a;}' OK
    #S = 'int main(){int a; int b; a = -5; b = 0; printd(a); return a;}' OK
    
    S = 'int main(){int a; int b; a = -5; b = 3; printd(a+b); return a;}'
    #S = 'int foo(int a, int b){return a + b;} int main() {int c; int d; c = -5; d = 0; return foo(c, d);}'
    
    #####################################
    #S = raw_input("Input expression: ")
    #S = "int main() {int i; i = 3 - 5; i = 3 + 5; i = 3 * 5; i = 3 / 5; i = 3 % 5;}" #Arithmetic operations ok
    #S = "int main() {int i; if(i>0){printf(i);}}"  #If statement ok
    #S = "int main() {int i; for(i=0;i<10;i=i+1){}}"  #For loop ok
    #S = "int main() {int i; i = 0; while(i<0){}}" #WHIle loop ok
    #S = "int main() {int i; do{i=1;} while(i<0);}" #Do While loop ok
    #S = "extern int foo2(int x, int y);int main() {int i; string k; if (i < 0) {int j; i = i + 1;}}" #Extern function ok
    #S = "extern int foo2(int x, int y);"
    #S = "int main() {int i; if (i < 0) {i = i + 1;}}" #If statement ok
    #S = "int main() {int i; if (k < 0) {i = i + 1;} else {}}" #If Else ok
    #S = 'int main(){int a, b, i; string k; a=5; b=10; k = "hi"; for(i=0;i<10;i=i+1){k = "no";}}'


    #source = sys.argv[-1]
    #S = open(source, "r").read()
    parser = parser_cstr.myparser
    ast = parser.parse(S)
    print ast
    print_tree(ast, 1)
    map(trav_tree, ast)
    print symbol_table
    print '\n'.join(assembly)

    
    
