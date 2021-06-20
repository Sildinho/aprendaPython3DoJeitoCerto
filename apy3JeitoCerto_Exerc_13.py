# -- coding utf-8 --
""" Exercício 13 - parametros, descompactação, variaveis - pag: 43 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from sys import argv

script, first, second, third = argv

print(">>>> argv =", repr(argv))
print()
print("O script é denominado:", script) # The script is called:
print("\nSua primeira variável é:", first) # Your first variable is: apple
print("Sua segunda variável é:", second) # Your second variable is: orange
print("Sua terceira variável é:", third) # Your third variable is: grapefruit(toranja)
print()
