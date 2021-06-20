# -- coding utf-8 --
""" Exercício 11 - fazendo perguntas - pag: 39 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """

print("1. Quantos anos você tem?", end=' ') # how old are you? o end=' ' mantem o cursor na mesma linha.
age = input()
print("2. Qual sua altura?", end=' ') # How tall are you?
height = input()
print("3. Quanto você pesa?", end=' ') # how much do you weigh?
weight = input()

print(f"\nEntão, você tem {age} anos, {height} de altura e {weight} de peso.\n") # So, you're 38 old, 190 tall and 105 heavy.  