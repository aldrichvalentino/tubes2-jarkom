all:
	@g++ -o main src/main.cpp

run:
	@./main

test:
	@./main < data/test.txt