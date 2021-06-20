# -- coding utf-8 --
""" Exercício 31 - tomando decisões - pag: 111 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
# Você entra em uma sala escura com dois dor. Você passa pela porta # 1 ou porta # 2?
print("""You enter a dark room with two dor. 
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.") # Tem um urso gigante comendo um bolo de queijo.1
    
    print("What do you do?") # O que você faz?
    print("1. Take the cake.") # Pegue o bolo.
    print("2. Scream at the bear.") # Grite com o urso.
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!") # O urso come sua cara. Bom trabalho!
    elif bear =="2":
        print("The bear eats your legs off. Good job!") # O urso come suas pernas. Bom trabalho!
    else:
        print(f"Well, doing {bear} is probaly better.") # Bem, fazer {urso} é provavelmente melhor.
        print("Bear runs away.") # Bear foge.

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.") # Você olha para o abismo sem fim na retina de Cthulhu.
    print("1. Blueberries.") # Amoras.
    print("2. Yellow jacket clothespins.") # Prendedores de roupa de jaqueta amarela.
    print("3. Understanding revolvers yelling melodies.") # Compreender revólveres gritando melodias.
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.") # Seu corpo sobrevive movido por uma mente de gelatina.
        print("Good job!") # Bom trabalho!
    else:
        print("The insanity rots your eyes into a pool of muck.") # A insanidade apodrece seus olhos em uma poça de lama.
        print("Good job!") # Bom trabalho!
else:
    print("You stumble around and fall on a knife and die. good job!") # Você tropeça, cai em uma faca e morre. bom trabalho!