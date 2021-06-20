# -- coding utf-8 --
""" Exercício 36 - criando e depurando - pag: 129 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
# dudu no podrão

from sys import exit


def hamburguer_supresa():
    print("\nQualé a música: Belo ou Wando?")

    opcao = input("\n> ".lower())

    if opcao == "belo":

        print("\nHamburguer simples")
        chatao("\tMó sem graça, tu!!.")

    elif opcao == "wando":
        print("\nX-Tesão com tudo dentro!! Gulosão!!")
        print("""
              Me suja de carmim,
              Me põe na boca o mel,
              Louca de amor,
              Me chama de céu,
              Oh! Oh! Oh! Oh! Oh!,
              E quando sai de mim,
              Leva meu coração,
              Você é fogo,
              Ou sou paixão!!!!!\n""")

    else:
        chatao("Po, cara!")


def trio_parada_dura():

    print("\nQual vai ser: Com ou Sem Barrerito?!")

    opcao = input("\n> ".lower())

    if opcao == "com":
        print("\nHamburguer com babata poutine e glacial.")
        print("\tTá decretado!!! Esse é raiz!!\n")

    elif opcao == "sem":
        print("\nBelo com batata murcha e refri quente!")
        chatao("\tFicou na fila pra isso?!")
    else:
        print("escolhe um aí")
        chatao("Po, cara!")


def dia_de_rock_bebe():

    print("\nBebê?")
    opcao = input("\n> ".lower())

    if opcao == "bebê" or "bebe":
        print("\nX-Tesão Quadruplo com Mega Poutine e uma Heineken + Estomasil.")
        print("\tMerece meu respeito!!!\n")
    else:
        balconista()


def chatao(pq):
    print(pq, "Chatão você enh!!!\n")
    exit(0)


def balconista():
    print("\nQue que tu quer?!")
    print("\nfala! Fala! fala! fala logooo!")
    print("\nQue que tu quer....\n")

    print("# 1. Hamburguer Supresa?")
    print("# 2. Trio Parada Dura")
    print("# 3. Dia de Rock Bebê")

    opcao = input("\n>  ".lower())

    if opcao == "1":  # hamburguer
        hamburguer_supresa()
    elif opcao == "2":  # trio
        trio_parada_dura()
    elif opcao == "3":  # trio top
        dia_de_rock_bebe()
    elif opcao >= "10":  # cliente casquinha
        print("\n Aêêêeee... casquinha de leite de texugo macho!!!!!\n")
        chatao("\tDemorou pacas pra isso??!!")
    else:
        chatao("\nCara, tu tem que se decidir logo ou sair da fila!!")


balconista()


"""
comentario para melhorar essa joça.

input("\n> ".lower())


Não lembro como o input funciona, mas caso assim não funcione talvez

input("\n> ").lower()


Ai funcionaria (acho) , pq o input vai fazer o que ?
1- Escrever na tela o que vc coloco dentro dele
2- Parar o programa até que alguem responda
3- Retornar o que a pessoa digitou.

Se vc quer tornar o que a pessoa digitou em minúsculo, faz sentido vc colocar fora pq ai é como se vc tivesse fazendo :
opcao = "Belo"
opcao_minuscula = opcao.lower() 


Sacou ?


Mas não lembro, se quiser testa fazendo
print(input("\n> ".lower()))
print(input("\n> ").lower())

ATENÇÃO A FORAMATAÇÃO



"""
