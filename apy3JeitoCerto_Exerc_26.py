# -- coding utf-8 --
""" Exercício 26 - parabens, faça um teste - pag: 97 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from sys import argv
# exercicio 12
print("How old are you?", end=' ')  # idade
age = input()
print("How tall are you?", end=' ')  # altura
height = input()
print("How much do you weigh?", end=' ')  # peso
weight = input()

# Então, você tem 38 anos, 1,9 de altura e 106 de peso.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
# exercicio 15
script, filename = argv

txt = open(filename) # nome arq + ex15_sample.txt

print(f"Here's your file {filename}:")  # aqui o arquivo
print(txt.read())

print("Type the filename again:")  # Digite o nome do arquivo novamente: use ex15_sample.txt
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")  # deu 5?


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


people = 20
cats = 30
dogs = 15


if people < cats:
    # Muitos gatos! O mundo está condenado!
    print("\nToo many cats! The world is doomed!")

if people < cats:
    # Não há muitos gatos! O mundo está salvo!
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")  # O mundo está babando!

if people > dogs:
    print("The world is dry!")  # O mundo esta seco


dogs += 5  # (20)

if people >= dogs:
    # tem mais gente que cachorro
    print("People are greater than or equal to dogs.")

if people <= dogs:
    # tem mais cachorro que gente
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")  # tá igual.
