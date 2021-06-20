# -- coding utf-8 --
""" Exercício 05 - mais variaveis e impressao - pag 23 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from colorama import Fore, Back, Style

# declarando as variaveis
name = 'Zed Shaw'.upper()  # nome
age = 35  # idade. pensa que tá velho.
height = 74 * 0.0254  # altura em polegadas (metros = 74*0.0254)
weight = 180 * 0.453592 # peso em libras (kg = 180*0.453592)
eyes = 'Azuis'.lower()  # olhos e com remela. hahahahahaa
teeth = 'Brancos'.lower()  # dentes branco.
hair = 'Castanho'.lower()  # cabelo castanho

# imprimindo as variaveis
print (f"\nVamos falar sobre {name}.") # Vamos falar sobre ...
print (f"{name} tem {age} anos.") # altura ... 1,87.
print (f"{name} tem {height:.2f} metros de altura.") # altura ... 1,87.
print (f"Ele pesa {weight:.1f} quilos.") # peso ... 81.
print ("\né bem magrelo para um americano.") # magrelo.
# sobre os olhos e cabelos.
print (f"\nEle tem olhos de {eyes} e cabelo de {hair}.")
# tomador de café.
print (f"Pode ser que seus dentes sejam {teeth}; dependende do café.")

# calculando uma varivel com variaveis
total = age + height + weight

# total de nada. sem sentido. to nem aí.
print (f"\nSomando: {age}; {height:.2f} e {weight:.1f} o total é {total:.0f}.\n")
