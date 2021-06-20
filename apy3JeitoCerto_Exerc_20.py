# -- coding utf-8 --
""" Exercício 20 - funções e arquivos - pag: 71 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n") # Primeiro, vamos imprimir o arquivo inteiro:

print_all(current_file)

print("\nNow let's rewind, kind of like a tape.") # Agora vamos rebobinar, como se fosse uma fita.

rewind(current_file)

print("\nLet's print three lines:") # Vamos imprimir três linhas

current_line = 1
print_a_line(current_line, current_file) # chama a linha tal do arquivo atual.

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
