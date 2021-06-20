# -- coding utf-8 --
# exemplos livro aprenda python 3 do jeito certo zed a. shaw - https://learnpythonthehardway.org/
# retirar as aspas triplas da parte que deseja ver ou copie para outro arquivo.
# Zen of Python

# import this # retire o comentario do import
"""
# exemplos livro aprenda python 3 do jeito certo - pag: 11

print("Hello World")
# print("Hello Again")
# print("I like typing this.")
print("This is fun.")
# print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')


# exemplos livro aprenda python 3 do jeito certo - pag: 14

# Um comentario, assim voce pode ler seu programa mais tarde.
# Qualquer coisa depois de # é ignorada pelo python.

print("I could have code like this.") # e o comentário depois é ignorado

# Você também pode usar um comentário para "desabilitar" um código:
# print("This will run")

print("This will run")


# exemplos livro aprenda python 3 do jeito certo - pag: 16

print("I will now count my chickens:")  # quantas galinhas

print("hens", 25 + 30 / 6.0)  # galinhas

print("Roosters", 100-25 * 3 % 4.0)  # galos

print("Now I will count the eggs:")  # ovos
print(3.0 + 2.0 + 1 - 5 + 4 % 2 - 1 / 4 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")  # 5 < -2 é falso
print(3 + 2 < 5 - 7)

print("What is 3+2?", 3 + 2.0)  # 5
print("What is 5-7?", 5 - 7.0)  # -2

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2.0)  # 5 maior que -2 - True
print("Is it greater or equal?", 5 >= -2.0)  # 5 maior ou igual a -2 - True
print("is it less or equal?", 5 <= -2.0)  # 5 menor ou igual a -2 - False


# exemplos livro aprenda python 3 do jeito certo - pag:


print("I will now count my chickens:")  # quantas galinhas

print("hens", 25+30 / 6)  # galinhas

print("Roosters", 100-25 * 3 % 4)  # galos

print("Now I will count the eggs:")  # ovos
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")  # 5 < -2 é falso
print(3 + 2 < 5 - 7)

print("What is 3+2?", 3+2)  # 5
print("What is 5-7?", 5-7)  # -2

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)  # 5 maior que -2 - True
print("Is it greater or equal?", 5 >= -2)  # 5 maior ou igual a -2 - True
print("is it less or equal?", 5 <= -2)  # 5 menor ou igual a -2 - False


# exemplos livro aprenda python 3 do jeito certo - testes
print("\n100 - 10% = ", 100-(100*0.1))
print("20 % 4 = ", 20 % 4)
print("20 % 4 = ", 20 // 4)

# exemplos livro aprenda python 3 do jeito certo - pag: 19

cars = 100  # int
space_in_a_car = 4.0  # float
drivers = 30  # motoristas
passengers = 90  # passageiros

cars_not_driven = cars - drivers  # carro parados
cars_driven = drivers  # carros com motorista
carpool_capacity = cars_driven * space_in_a_car  # capacidade de passageiros = 120
average_passengers_per_car = passengers / \
    cars_driven  # passageiros por carro = 90

print("\nthere are", cars, "cars available.")
print("There are only", drivers, "drivers availableself.")
print("there will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.\n")

# exemplos livro aprenda python 3 do jeito certo - testes

A = 10
B = 15
C = 25
a = A/2.0
b = B/2.0
c = C/2.0

D = (A*c)+(a**b)-C*c/b**c

print("D = %.3f" % D + "\n")

# exemplos livro aprenda python 3 do jeito certo - pag: 37

Teste_1 = "Teste de paragrafo 1."
Teste_2 = "\aTeste de paragrafo 2."
Teste_3 = "\bTeste de paragrafo 3."
Teste_4 = "\fTeste de paragrafo 4."
Teste_5 = "\rTeste de paragrafo 5."
Teste_6 = "\tTeste de paragrafo 6."
Teste_7 = "\vTeste de paragrafo 7."
Teste_8 = "\000Teste de paragrafo 8."

print("Teste 1 =", Teste_1)
print("Teste 2 =", Teste_2)
print("Teste 3 =", Teste_3)
print("Teste 4 =", Teste_4)
print("Teste 5 =", Teste_5)
print("Teste 6 =", Teste_6)
print("Teste 7 =", Teste_7)
print("Teste 8 =", Teste_8)


# exemplos livro aprenda python 3 do jeito certo - pag: 64

def fruta():
    print("\nBanana")

def preparo_alimento(arg1):
    print(f"{arg1}")


#fruta() + preparo_alimento("frita")
fruta(), preparo_alimento("frita")
#fruta(); preparo_alimento("frita")

# exemplos livro aprenda python 3 do jeito certo - pag: 77


def mais(a, b):
    print(a + b)

mais(5, 3)

print(24+34/100 - 1023)

# exemplos livro aprenda python 3 do jeito certo - pag: 79

print("\ncalc 1% = ", 100*0.01 )
print("calc 2% = ", 100*0.02 )
print("calc 3% = ", 100*0.03 )
print("calc 4% = ", 100*0.04 )
print("calc 5% = ", 100*0.05 )
print("calc 10% = ", 100*0.10 )
print("calc 15% = ", 100*0.15 )

print("{}"*15)
print("& - % - $ - @"*10)

# exemplos livro aprenda python 3 do jeito certo - pag: 84

print(0b1011010)
print(ord('Z'))
print(chr(90))
#print(chr[90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119])



# exemplos livro aprenda python 3 do jeito certo - pag: 112

print("Abro a geladeira.")
print("olho a caixa de ovos #1 ou a caixa de leite #2? ")

caixa = input ("> ")

if caixa == "1":
    print("Oba! tem ovos.")
    print("O que eu vou fazer?")
    print("1. Faço um bolo?")
    print("2. Faço um omelete?")
    
    fome = input ("> ")
    
    if fome == "1":
        print("To sem pressa. vou fazer um bolo.")
    elif fome == "2":
        print("vou de omelete que é mais rapido!")
    else:
        print("Sacanagem os ovos estão podres.")

elif caixa == "2":
    print("vou de leite!!")
    print("1. bebo todo leite?")
    print("2. faço chocolate quente?")
    
    sede = input ("> ")
    
    if sede == "1":
        print("Quem deixou a caixa de leite fazia na geladeira??!!")
    elif sede == "2":
        print("chocolate quente no frio é show.")
    else:
        print("Derramei o leite. que desastrado.")
else:
    print("Geladeira vazia! foi mal.")



# exemplos livro aprenda python 3 do jeito certo - pag: 116

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

print('*'*30)

for i in elements:
    print(f"Element was: {i}")
"""

# exemplos livro aprenda python 3 do jeito certo - pag: 120
"""
i = 0
numbers = []
while i < 2:
    print(f"\nAt the top is {i}") # No topo está... 0
    numbers.append(i)

    i = i+1
    print("Numbers now: ", numbers) # Números agora... 0
    print(f"At the cottom i is {i}") # No caso, i é... 1

print("\nThe numbers: ")

for num in numbers:
    print(num)

print("*"*50)


def fruta():
    print("banana")
fruta()

def potencia(base, expoente):
    resposta = base**expoente
    return resposta
print(potencia(3,2))

i = 0
numbers = []

while i < 6:
    print(f"At the top is {i}")
    numbers.append(i)

    i = i+1
    print("Numbers now: ", numbers)
    print(f"At the cottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)




# exemplos livro aprenda python 3 do jeito certo - pag: 123 e 124

animals = ['bear', 'tiger', 'penguin', 'zebra']
print(animals[0]) #bear

animals = ['bear', 'python3', 'peacock', 'kangaroo', 'whale', 'platypus', 'alligator', 'armadillo', 'bat', 'elephant', 'butterfly', 'camel', 'hippopotamus', 'chameleon', 'goat', 'chicken', 'owl' 'Donkey', 'Monkey']
lista = sorted(animals)
print("ordem alfabetico =",lista)
print("Inserido =", animals)

#print(animals.count())
print(f"O primeiro (1º) animal está em 0 e é um", animals[0].upper())
print(f"O segundo (2º) animal está em 1 e é um", animals[1].lower()) # não é um animal.
print(f"O terceiro (3º) animal está em 2 e é um", animals[2].capitalize())
print(f"O quarto (4º) animal está em 3 e é um", animals[3].upper())
print(f"O quinto (5º) animal está em 4 e é um", animals[4].upper())
print(f"O sexto (6º) animal está em 5 e é um", animals[5].upper())

"""
# exemplos livro aprenda python 3 do jeito certo - pag: 143
"""
>>> things = ['a', 'b', 'c', 'd']
>>> print(things[1])
b   
>>> things[1] = 'z'
>>> things
['a', 'z', 'c', 'd']
"""

"""
>>> stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
>>> print(stuff['name'])  
Zed
>>> print(stuff['age'])
39  
>>> print(stuff['height'])
74  
>>> stuff['city'] = 'SF'
>>> print(stuff['city'])
SF
>>> print(stuff) 
{'name': 'Zed', 'age': 39, 'height': 74, 'city': 'SF'}
"""

"""
>>> stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
>>> print(stuff['name']) 
Zed
>>> print(stuff['age'])
39
>>> print(stuff['height'])
74
>>> stuff['city'] = 'SF'
>>> print(stuff['city'])
SF
>>> stuff[1] = "Wow"
>>> stuff[2] = "Neato"
>>> print(stuff[1])
Wow
>>> print(stuff[2])
Neato
>>> del stuff['city']
>>> del stuff[1]
>>> del stuff[2]
>>> stuff
{'name': 'Zed', 'age': 39, 'height': 74}



# exemplos livro aprenda python 3 do jeito certo - pag: 149
#ex40a.py
mystuff = {'apple': "I AM APPLES!", 'alligator':"I'm an alligator", 'astronaut':"I'm an astronaut"}
print(mystuff['apple'])
print(mystuff['alligator'].lower())
print(mystuff['astronaut'].upper())

lista_1 = ['a', 'h', 'd', 'z', 'c', 'f', 'e', 'b', ]
lista_1.reverse()
print(lista_1)
lista_1.sort()
print(lista_1)
lista_1.insert(6,'g')
lista_1.insert(13,'v')
print(lista_1)
lista_1.append('x')
lista_1.append('y')
lista_1.sort()
print(lista_1)


# exemplos livro aprenda python 3 do jeito certo - pag: 153

class Musiquinha(object):

    def __init__(self, letras):
        self.letras = letras

    def toque_a_musica(self): 
        for trexo in self.letras:
            print(trexo)

orquestra_bichos = Musiquinha(["Có, có, có",
                            "Có, có, có, có, có, có, có",
                            "Có, có, có",
                            "Có, có, có, có, có, có, có\n",
                            "A galera explodiu, foi assim que surgiu",
                            "A galinha cantora mais famosa do brasil",
                            "A galera explodiu, foi assim que surgiu",
                            "A galinha cantora mais famosa do brasil",
                            "by patati patata\n"])

borboletinha = Musiquinha(["Borboletinha tá na cozinha",
                            "Fazendo chocolate para a madrinha",
                            "Poti, poti",
                            "Perna de pau",
                            "Olho de vidro",
                            "E nariz de pica-pau (pau, pau)",
                            "by eliana\n"])
orquestra_bichos.toque_a_musica()

borboletinha.toque_a_musica()


# exemplos livro aprenda python 3 do jeito certo - pag: 182

# ex44a.py - herança implicita
class Parent(object):
    def implicit (self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad = parent = implicit
son = child = parent = implicit


# ex44b.py - sobrescreva explicitamente

class Parent(object):
    def override (self):
        print("PARENT override()")
        print("\tchamou o pai\n")

class Child(Parent):
    def override (self):
        print("CHILD override(filho)")
        print("\tchamou o filho\n")

dad = Parent()
son = Child()

dad.override()
son.override()

son = Parent()
# dad = Child()

son.override() # filho
# dad.override()

# dad = parent = override
# son = child = parent = override

# ex44c.py - altere antes ou depois

class Parent(object):
    def altered (self):
        print("PARENT altered(pai)\n")

class Child(Parent):
    def altered (self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self)#.altered()
        print("\tCHILD, AFTER PARENT altered()\n")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# dad = parent = altered
# son = child = parent = altered = super

# ex44d.py - os tres combinados

class Parent(object):

    def override (self):
        print("PARENT override()\n")

    def implicit (self):
        print("PARENT implicit()\n")

    def altered (self):
        print("PARENT altered()\n")

class Child(Parent):
    
    def override (self):
        print("CHILD override()\n")
        
    def altered (self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("\tCHILD, AFTER PARENT altered()\n")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


# ex44e.py - composição

class Other(object):
    
    def override (self):
        print("\tOTHER override(outro)\n")

    def implicit (self):
        print("\nOTHER implicit(outro)\n")

    def altered (self):
        print("\n\tOTHER altered(outro)\n")

class Child(object):
    
    def __init__ (self):
        self.other = Other()
    
    def implicit (self):
        self.other.implicit()
    
    def override (self):
        print("CHILD override(filho)\n")
        self.other.override()
    
    def altered (self):
        print("CHILD, BEFORE OTHER altered(filho)")
        self.other.altered()
        print("\t\tCHILD, AFTER OTHER altered(filho)\n")


son = Child()

son.implicit()
son.override()
son.altered()

# http://pytthon.org/dev/peps/pep-0008/

"""
# exemplos livro aprenda python 3 do jeito certo - pag: XX

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print(Fore.BLUE + 'some blue text')
print(Style.RESET_ALL)
print(Back.YELLOW + 'more blue texts')
print(Style.RESET_ALL)

print(Fore.BLACK + 'some red text')
print(Back.WHITE + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)

print('back to normal now')


# exemplos livro aprenda python 3 do jeito certo - pag: 15



# exemplos livro aprenda python 3 do jeito certo - pag: 15


# exemplos livro aprenda python 3 do jeito certo - pag: 15


# exemplos livro aprenda python 3 do jeito certo - pag: 15


# exemplos livro aprenda python 3 do jeito certo - pag: 15