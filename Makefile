all:
	@g++ -o main.exe src/main.cpp

run:
	@./main.exe

test:
	@./main.exe < data/test.txt
