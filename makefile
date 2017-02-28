.PHONY: all
all: 
	python -m compiler < registers/test/add.c > add.s
	python -m compiler < registers/test/cond.c > cond.s
	python -m compiler < registers/test/div.c > div.s
	python -m compiler < registers/test/eratoCPP.c > erato.s
	python -m compiler < registers/test/expr.c > expr.s
	python -m compiler < registers/test/functions.c > functions.s
	python -m compiler < registers/test/loops.c > loops.s
	python -m compiler < registers/test/lsh.c > lsh.s
	python -m compiler < registers/test/mod.c > mod.s
	python -m compiler < registers/test/mul.c > mul.s
	python -m compiler < registers/test/neg.c > neg.s
	python -m compiler < registers/test/rsh.c > rsh.s
	python -m compiler < registers/test/stringCPP.c > string.s
	python -m compiler < registers/test/string2CPP.c > string2.s
	python -m compiler < registers/test/sub.c > sub.s

.PHONY: bin
bin:
	gcc add.s lib.c -o add
	gcc cond.s lib.c -o cond
	gcc div.s lib.c -o div 
	gcc erato.s lib.c -o erato
	gcc expr.s lib.c -o expr
	gcc functions.s lib.c -o functions
	gcc loops.s lib.c -o loops
	gcc lsh.s lib.c -o lsh
	gcc mod.s lib.c -o mod
	gcc mul.s lib.c -o mul
	gcc neg.s lib.c -o neg
	gcc rsh.s lib.c -o rsh
	gcc string.s lib.c -o string
	gcc string2.s lib.c -o string2
	gcc sub.s lib.c -o sub


.PHONY: exall
exall:
	./add
	./cond
	./div
	./erato
	./expr
	./functions
	./loops
	./lsh
	./mod
	./mul
	./neg
	./rsh
	./string
	./string2
	./sub	