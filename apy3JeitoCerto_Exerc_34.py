# -- coding utf-8 --
""" Exercício 34 - acessando os elementos das listas - pag: 123 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
import re

animals = ['bear', 'tiger', 'penguin', 'zebra']
print(animals[0]) #bear

animals = ['bear', 'python3', 'peacock', 'kangaroo', 'whale', 'platypus']
print(animals)
print(f"O primeiro (1º) animal está em 0 e é um", animals[0].upper())
print(f"O segundo (2º) animal está em 1 e é um", animals[1].upper()) # não é um animal.
print(f"O terceiro (3º) animal está em 2 e é um", animals[2].upper())
print(f"O quarto (4º) animal está em 3 e é um", animals[3].upper())
print(f"O quinto (5º) animal está em 4 e é um", animals[4].upper())
print(f"O sexto (6º) animal está em 5 e é um", animals[5].upper())

print("* "*40)

print(f"O animal em 0 é o 1º e é um",animals[0].lower())
print(f"O animal em 1 é o 2º e é um",animals[1].lower()) # não é um animal.
print(f"O animal em 2 é o 3º e é um",animals[2].lower())
print(f"O animal em 3 é o 4º e é um",animals[3].lower())
print(f"O animal em 4 é o 5º e é um",animals[4].lower())
print(f"O animal em 5 é o 6º e é um",animals[5].lower())