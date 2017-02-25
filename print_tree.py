
def print_tree(t, i):
    
    if type(t) == list or type(t) == tuple:
        i += 1       
        for item in t:
            print_tree(item, i)
    else:
        print " "* i, t
        

        
def is_str_op(t):
    flag = False

        
    if type(t) == list or type(t) == tuple:      
        for item in t:
            if is_str_op(item):
                flag = True
        return flag
    else:
        return t == "CONST_STRING"
    
