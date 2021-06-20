# -- coding utf-8 --
""" Exercício 15 - lendo arquivos - pag: 51 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from sys import argv

script, filename = argv
txt = open(filename) # abrir (nome do arquivo)

print(f"Here's your file {filename}:") # Aqui está seu arquivo {nome do arquivo}
print(txt.read())

print("Type the filename again:") # Digite o nome do arquivo novamente
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
