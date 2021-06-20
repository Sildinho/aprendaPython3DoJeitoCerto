# -- coding utf-8 --
""" Exercício 35 - desvios e funções - pag: 125 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?") # Esta sala está cheia de ouro. Quanto você pega?

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.") # digite um número.

    if how_much < 50:
        print("Nice, you're not greedy, you win!") # você venceu!
        exit(0)
    else:
        dead("You greedy bastard!") # ganancioso


def bear_room():
    print("Thre is a bear here.") # tem urso aqui.
    print("The bear has a bunch of honey.") # o urso tem muito mel
    print("The fat bear is in front of another door.") # o urso gordo esta na porta
    print("How are you going to move the bear?") # como tirar o urso?
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "Take honey":
            dead("The bear looks at you then slaps your face off.") # o urso tá agressivo
        elif choice == "taunt bear" and not bear_moved: # mexer com o urso e
            print("The bear has noved from the door.") # o urso saiu da porta
            print("You can go through it now.") # pode passar.
            bear_moved = True
        elif choice == "taunt bear" and bear_moved: # mexer com o urso
            dead("The bear gets pissed off and chews your leg off.") # urso ataca e morde a perna.
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.") # Não sai o que significa. erro.

def cthulhu_room():
    print("Here you see the great evil Cthulhu.") # Aqui você vê o grande monstro chamado Cthulhu
    print("He, it, whatever stares at you and you go insane.") # "Ele, aquilo, tudo o que olha para você e você enlouquece.
    print("Do you flee for your life or eat your head?") # Você foge para salvar sua vida ou come sua cabeça?

    choice = input("> ")

    if "flee" in choice: # volta pro inicio
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!") # isso aí!!!
    exit(0)

def start():
    print("You are in dark room.") # "Você está em um quarto escuro
    print("There is a dor to your right and left.") # tem portas na direita e esquerda
    print("which on do you take?") # vai em qual?

    choice = input("> ")

    if choice == "left": # saal do urso
        bear_room()
    elif choice == "right": # sala do diabo Cthulhu
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.") # cambeia ate morrer.

start()
