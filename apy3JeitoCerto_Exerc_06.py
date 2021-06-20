# -- coding utf-8 --
""" Exercício 06 - string e texto - pag. 25 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from colorama import Fore, Back, Style

types_of_people = 10 
x = f"\nThe are {types_of_people} types of people." # Existem 10 tipos de pessoas.

binary = "binary"
do_not = "don't"
#y = f"\nThose who know {binary} and those who {do_not}." # que sabem ou nao binario.
y = f"\nAqueles que sabem {binary} e aqueles que {do_not}." # Those who know binary and those who don't.

print(x) # Existem 10 tipos de pessoas.
print(y) # que sabem ou nao binario.

print(f"\nEu disse: {x}") # Existem 10 tipos de pessoas.
print(f"Eu também disse:'{y}'") # que sabem ou nao binario.

print(Fore.BLUE)
hilarious = not False # negativa.
joke_evaluation = "Essa piada não é tão engraçada?! {}" # piadinha de m...
print(joke_evaluation.format(hilarious))
print(Style.RESET_ALL)

w = "This is the left side of... " # concatenando
e = "a string with a right side."
print(w + e, "\n")