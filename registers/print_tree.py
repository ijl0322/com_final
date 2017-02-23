
def print_tree(t, i):
    
    if type(t) == list or type(t) == tuple:
        i += 1       
        for item in t:
            print_tree(item, i)
    else:
        print " "* i, t
        
    
##rint type((3,3))
##tree = [('DEF_FUNC', ('TYPE', 'int'), ('main', None), ('COMP_STATE', [(('TYPE', 'int'), [('IDENT', 'a'), ('IDENT', 'b'), ('IDENT', 'i')]), (('TYPE', 'string'), [('IDENT', 'k')]), ('STATE', ('ASSIGN', 'a', ('CONST_INT', '5'))), ('STATE', ('ASSIGN', 'b', ('CONST_INT', '10'))), ('STATE', ('ASSIGN', 'k', ('CONST_STRING', '"hi"'))), ('STATE', ('FOR', ('ASSIGN', 'i', ('CONST_INT', '0')), ('<', ('IDENT', 'i'), ('CONST_INT', '10')), ('ASSIGN', 'i', ('PLUS', ('IDENT', 'i'), ('CONST_INT', '1'))), ('STATE', ('COMP_STATE', [('STATE', ('ASSIGN', 'k', ('CONST_STRING', '"no"')))]))))]))]

##print_tree(tree, 1)