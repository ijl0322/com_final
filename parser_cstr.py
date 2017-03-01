import ply.yacc as yacc
from scanner import tokens
import sys
import project1_preprocessor as preprocessor

symbol_table = [{"scope":"function parameter"},{"scope":"extern"},{"scope":"global"}]
out_of_scope = []

i = 1

def print_symbol_table(scope_dic):
    print "\nScope: ", scope_dic["scope"] 
    print "---------------------------"
    print "Variable name        Type"
    print "---------------------------"
    for var in scope_dic:
        if var != "scope":
            var_type = scope_dic[var]['type']
            if type(var_type) == list:
                var_type = (", ").join(var_type)        
            print var + " "*(21-len(var)) + var_type            
    print "\n"

precedence = ( ('nonassoc', 'IF_STATE'), ('nonassoc', 'ELSE')) 

def p_program_1(t):
    '''program : external_declaration'''
    t[0] = [t[1]]
    return t[0]

def p_program_2(t):
    '''program : program external_declaration'''
    t[0] = t[1] + [t[2]]
    return t[0]

### external-declaration:

def p_external_declaration_1(t):
    '''external_declaration : declaration'''
    t[0] = t[1]

def p_external_declaration_2(t):
    '''external_declaration : EXTERN declaration'''
    t[0] = ('EXTERN', t[2])
    #print "Declaring extern function", (t[2][1][0][1][0]) 
    #symbol_table[1][(t[2][1][0][1][0])] = {"type":[t[2][0][1], "function"]}

def p_external_declaration_3(t):
    '''external_declaration : function-definition'''
    t[0] = t[1]

### function

def p_function(t):
    '''function-definition : type function_declarator compound_instruction''' 
    t[0] = 'DEF_FUNC', t[1], t[2], t[3]
    #print "Declaring function %s" %(t[2][0])
    symbol_table[-1][t[2][0]] = {"type":[t[1][1], "function"]}
    
### declaration

def p_declaration(t): # multiple variable declaration on the same line ??? 
    '''declaration : type declarator_list SEMI_COL'''
    t[0] = ('DEC_VAR',t[1], t[2])
    for var in t[2]:
        if var[0] == 'IDENT' and type(var[1]) == str:
            #print "Declaring variable %s of type %s" %(var[1], str(t[1][1]))
            symbol_table[-1][(var[1])] = {"type":str(t[1][1])}


### type

def p_type(t):
    '''type : INT
            | STRING'''
    t[0] = t[1]  

### declarator list

def p_declarator_list_1(t):
    '''declarator_list : declarator'''
    t[0] = [t[1]]
    
def p_declarator_list_2(t):
    '''declarator_list : declarator_list COMMA declarator'''
    t[0] = t[1] + [t[3]]    

### declaration_list

def p_declaration_list_1(t):
    '''declaration_list : declaration'''
    t[0] = [t[1]]

def p_declaration_list_2(t):
    '''declaration_list : declaration_list declaration'''
    t[0] = t[1] + [t[2]]
    
### declarator 

def p_declarator(t):
    '''declarator : IDENT
                    | function_declarator'''
    t[0] = ('IDENT',t[1])

### function_declare

def p_function_declarator_1(t):
    '''function_declarator : IDENT L_PARENTHESIS R_PARENTHESIS'''
    t[0] = (t[1], None)

def p_function_declarator_2(t):
    '''function_declarator : IDENT L_PARENTHESIS parameter_list R_PARENTHESIS'''
    t[0] = (t[1], t[3])
    for var in t[3]:
        symbol_table[0][var[1]] = {"type":var[0][1]}

### parameter_list

def p_parameter_list_1(t):
    '''parameter_list : parameter_declaration'''
    t[0] = [t[1]]

def p_parameter_list_2(t):
    '''parameter_list : parameter_list COMMA parameter_declaration'''
    t[0] = t[1] + [t[3]]

### parameter_declaration

def p_parameter_declaration(t):
    '''parameter_declaration : type IDENT'''
    t[0] = t[1], t[2]

### instruction
def p_instruction_1(t):
    '''instruction : SEMI_COL'''
    t[0] = ('STATE', None)

def p_instruction_2(t):
    '''
    instruction : compound_instruction
              | expression_instruction
              | iteration_instruction
              | select_instruction
              | jump_instruction
              '''
    t[0] = ('STATE', t[1])

### expression_instruction
def p_expression_instruction_1(t):
    '''expression_instruction : expression SEMI_COL'''
    t[0] = t[1]

def p_expression_instruction_2(t):
    '''expression_instruction : assignment SEMI_COL'''
    t[0] = t[1]
    
### assignment

def p_assignment(t):
    '''assignment : IDENT ASSIGNMENT expression'''
    t[0] = ('ASSIGN', t[1], t[3])
    #print "Assigning ", t[1], t[3]
    #for table in symbol_table[:0:-1]:
    #    if t[1] in table:
    #        if table[t[1]]["type"] == "int" and t[3][0] == "CONST_INT":
    #            table[t[1]]["value"] = t[3][1]
    #            break
    #        elif table[t[1]]["type"] == "string" and t[3][0] == "CONST_STRING":
    #            table[t[1]]["value"] = t[3][1]
    #            break
    #        else:
    #            raise ValueError("Variable %s is of type %s, cannot assign value %s" %(t[1], table[t[1]]["type"], str(t[3][1])))
            
    

### compound_instruction

def p_compound_instruction_1(t):
    '''compound_instruction : block_start declaration_list instruction_list block_end'''
    t[0] = ('COMP_STATE', t[2] + t[3])

def p_compound_instruction_2(t):
    '''compound_instruction : block_start declaration_list block_end'''
    t[0] = ('COMP_STATE', t[2])

def p_compound_instruction_3(t):
    '''compound_instruction : block_start instruction_list block_end'''
    t[0] = ('COMP_STATE', t[2])
    
def p_compound_instruction_4(t):
    '''compound_instruction : block_start block_end'''
    t[0] = ('COMP_STATE', [])
    
### block

def p_block_start(t):
    '''block_start : LEFT_BRACKET'''
    t[0] = t[1]
    global i
    symbol_table.append({"scope": "block local " + str(i)})
    i += 1
    #print "added scope"
    #print symbol_table


def p_block_end(t):
    '''block_end : RIGHT_BRACKET'''
    t[0] = t[1]
    out_of_scope.append(symbol_table.pop())
    #print "remove_scope"
    #print symbol_table
    #print out_of_scope

### instruction_list:

def p_instruction_list_1(t):
    '''instruction_list : instruction'''
    t[0] = [t[1]]

def p_instruction_list_2(t):
    '''instruction_list : instruction_list instruction'''
    t[0] = t[1] + [t[2]]

### select_instruction

def p_select_instruction_1(t):
    '''select_instruction : cond_instruction instruction %prec IF_STATE''' #
    t[0] = ('IF', t[1], t[2])
    ##print "Define if statement with condition", t[1][1][1][1], t[1][1][0], t[1][1][2][1]
    
def p_select_instruction_2(t):
    '''select_instruction : cond_instruction instruction ELSE instruction''' #
    t[0] = ('ELSE', t[1], t[2], t[4])
    ##print "Define If Else statement with condition", t[1][1][1][1], t[1][1][0], t[1][1][2][1]


### condition_instruction

def p_cond_instruction(t):    
    '''cond_instruction : IF L_PARENTHESIS condition R_PARENTHESIS''' 
    t[0] = t[3]

### iteration_instruction

def p_iteration_instruction_1(t):
    '''iteration_instruction : WHILE L_PARENTHESIS condition R_PARENTHESIS instruction'''
    t[0] = ('WHILE', t[3], t[5])
    #print "Define While loop with condition", t[3][1][1], t[3][0], t[3][2][1]

def p_iteration_instruction_2(t):
    '''iteration_instruction : DO instruction WHILE L_PARENTHESIS condition R_PARENTHESIS SEMI_COL'''
    t[0] = ('DO_WHILE', t[2], t[5])
    #print "Define Do While loop with condition", t[5][1][1], t[5][0], t[5][2][1]
    
def p_iteration_instruction_3(t):
    '''iteration_instruction : FOR L_PARENTHESIS assignment SEMI_COL condition SEMI_COL assignment R_PARENTHESIS instruction '''
    t[0] = ('FOR', t[3], t[5], t[7], t[9])
    #print "Define For loop with iterator", t[3][1]
    
### jump_instruction

def p_jump_instruction(t):
    '''jump_instruction : RETURN expression SEMI_COL'''
    t[0] = ('RETURN', t[2])
    
### condition

def p_condition(t):
    '''condition : expression comparison_operator expression'''
    t[0] = (t[2], t[1], t[3])
    #print t[0]
    
def p_condition2(t):
    '''condition : expression'''
    if t[1][0] != "CALL_FUNC" or (t[1][1] != "eq" and t[1][1] != "ne"):
        raise ValueError("There is an issue with your grammar")
    t[0] = t[1]

            
### comparison_operator
    
def p_comparison_operator(t):
    '''comparison_operator : EGAL
                        | DIFF
                        | INF 
                        | SUP 
                        | INFEQUAL
                        | SUPEQUAL '''
    #print "comp"
    t[0] = t[1]

### expression

def p_expression_1(t):
    '''expression : expression_additive'''
    #print "expression"
    t[0] = t[1]

def p_expression_2(t):
    '''expression : expression SHIFTLEFT expression_additive'''
    t[0] = ('SHIFTLEFT', t[1], t[3])

def p_expression_3(t):
    '''expression : expression SHIFTRIGHT expression_additive'''
    t[0] = ('SHIFTRIGHT', t[1], t[3])

### expression_additive

def p_expression_additive_1(t):
    '''expression_additive : expression_multiplicative'''
    #print "add"
    t[0] = t[1]

def p_expression_additive_2(t):
    '''expression_additive : expression_additive PLUS expression_multiplicative'''
    t[0] = ('PLUS', t[1], t[3])
    #print "Addition of %s and %s" %(t[1][1], t[3][1])

def p_additive_expression_3(t):
    'expression_additive : expression_additive MINUS expression_multiplicative'
    t[0] = ('MINUS', t[1], t[3])
    #print "Subtraction of %s and %s" %(t[1][1], t[3][1])

### expression_multiplicative

def p_expression_multiplicative_1(t):
    'expression_multiplicative : unary_expression'
    #print "mult"
    t[0] = t[1]

def p_expression_multiplicative_2(t):
    'expression_multiplicative : expression_multiplicative MULTI unary_expression'
    t[0] = 'MUL', t[1], t[3]
   # print "Multiplication of %s and %s" %(t[1][1], t[3][1])

def p_expression_multiplicative_3(t):
    'expression_multiplicative : expression_multiplicative DIV unary_expression'
    t[0] = 'DIV', t[1], t[3]
    #print "Division of %s and %s" %(t[1][1], t[3][1])

def p_multiplicative_expression_4(t):
    'expression_multiplicative : expression_multiplicative MODULO unary_expression'
    t[0] = 'MODULO', t[1], t[3]
    #print "Modulo operation of %s and %s" %(t[1][1], t[3][1])

### unary_expression

def p_unary_expression_1(t): #numeric values? 
    '''unary_expression : postfix_expression'''
    #print "unary"
    t[0] = t[1]

def p_unary_expression_2(t): #negative numeric values? 
    '''unary_expression : MINUS unary_expression'''
    
    #if t[2][0] == 'CONST_INT':
    #    t[0] = (t[2][0], str(int(t[2][1]) * -1))
    
    t[0] = ('NEG',t[2])
    
### postfix_expression

def p_postfix_expression_1(t):
    '''postfix_expression : primary_expression'''
    #print "postfix"
    t[0] = t[1]

def p_postfix_expression_2(t):
    '''postfix_expression : IDENT L_PARENTHESIS argument_expression_list R_PARENTHESIS'''
    t[0] = ('CALL_FUNC',t[1], t[3])    
    #print "Calling function %s" %(t[1])
    
def p_postfix_expression_3(t):
    '''postfix_expression : IDENT L_PARENTHESIS R_PARENTHESIS'''
    t[0] = ('CALL_FUNC',t[1], None)    
    #print "Calling function %s" %(t[1])    

### argument_expression

def p_argument_expression_list_1(t):
    '''argument_expression_list : expression'''
    t[0] = [t[1]]
    
def p_argument_expression_list_2(t):
    '''argument_expression_list : argument_expression_list COMMA expression'''
    #put the expressions into one list ?
    t[0] = t[1] + [t[3]]
    
### primary_expression

def p_primary_expression_1(t):
    '''primary_expression : IDENT'''
    t[0] = ('IDENT', t[1])

def p_primary_expression_2(t):
    '''primary_expression : CONST_INT'''
    t[0] = ('CONST_INT',t[1])
    
def p_primary_expression_3(t):
    '''primary_expression : CONST_STRING'''
    t[0] = ('CONST_STRING', t[1])

def p_primary_expression_4(t):
    '''primary_expression : L_PARENTHESIS expression R_PARENTHESIS'''
    t[0] = ('PRIME_EXPR',t[2])
    
def p_primary_expression_5(t):
    '''primary_expression : CHAR'''
    char = t[1].replace("'", '"')
    t[0] = ('CHAR', char)
    
    
### test_case remove later
#def p_expression(t):
#    '''expression : primary_expression'''
#    t[0] = t[1]
    
def p_error(t):
    if t:
         raise ValueError("Syntax error at %s" %t)
    else:
         print("Syntax error at EOF")

myparser = yacc.yacc(method='LALR')

if __name__ == '__main__':
    #S = raw_input("Input expression: ")
    #S = "int main() {int i; i = 3 - 5; i = 3 + 5; i = 3 * 5; i = 3 / 5; i = 3 % 5;}" #Arithmetic operations ok
    #S = "int main() {int i; if(i>0){printf(i);}}"  #If statement ok
    #S = "int main() {int i; for(i=0;i<10;i=i+1){}}"  #For loop ok
    #S = "int main() {int i; i = 0; while(i<0){}}" #WHIle loop ok
    #S = "int main() {int i; do{i=1;} while(i<0);}" #Do While loop ok
    #S = "extern int foo2(int x, int y);int main() {int i; string k; if (i < 0) {int j; i = i + 1;}}" #Extern function ok
    #S = "extern int foo2(int x, int y);"
    #S = "int main() {int i; if (i < 0) {i = i + 1;}}" #If statement ok
    #S = "int main() {int i; if (k < 0) {i = i + 1;}}" #If Else ok
    S = 'int main(){printf(27+"M");return 0;c}'
    #S = 'int main(){int a, b, i; string k; a=5; b=10; k = "hi"; for(i=0;i<10;i=i+1){k = "no";}}'
    #S = "int main(){int a; a = -5; return a;}int foo(){}"

    #source = sys.argv[-1]
    #source = "registers/test/opti.c"
    #S = open(source, "r").read()
    parser = yacc.yacc(method='LALR') 
    
    print parser.parse(preprocessor.delete_comments(S))
    print "\n\nSymbol Tables: "
    for scopes in symbol_table:
        if len(scopes) != 1:
            print_symbol_table(scopes)
    for scopes in out_of_scope:
        if len(scopes) != 1:
            print_symbol_table(scopes)
