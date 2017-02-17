import parser_cstr
from print_tree import print_tree
from functools import partial






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
    #S = "int main() {int i; if (k < 0) {i = i + 1;} else {}}" #If Else ok
    #S = 'int main(){int a, b, i; string k; a=5; b=10; k = "hi"; for(i=0;i<10;i=i+1){k = "no";}}'
    S = "int main(){int a; a = -5; return a;}int foo(){}"

    #source = sys.argv[-1]
    #S = open(source, "r").read()
    parser = parser_cstr.myparser
    ast = parser.parse(S)
    print_tree(ast, 1)
    
    

