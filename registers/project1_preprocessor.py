import re

def delete_comments(source):
    comment = re.compile(r'/\*.*\*/', re.DOTALL)
    single_comment = re.compile(r'//.*')
    result = re.sub(comment, "\n", source)
    result = re.sub(single_comment, "\n", result)
    return result

def replace_macro(source):
    src_code = source
    macro = re.compile(r'#define [A-Z]+ [a-zA-Z0-9]+')
    ##result = re.match(macro, source)
    for i in re.findall(macro, source):
        ##print i
        src_code = src_code.replace(i, " ")
        macro_tokens = i.split()
        var_name = macro_tokens[1]
        var_val = macro_tokens[2] 
        src_code = src_code.replace(var_name, var_val)

    return src_code

