# -- coding utf-8 --
# exemplos livro aprenda python 3 do jeito certo - pag: 107 a 113
# Exercício 29 - pag: 107 - Estrutura de condição if
bala = 4
chocolate = 30

if bala < chocolate:
    print("\ntenhos mais chocolate.")
else:
    print("\nTenho mais balas.")

print("*"*60)
# Exercício 30 - pag: 109 - Estrutura de condição if

idade = 17

if idade < 18:
    print("Nao pode entrar na festa.")
else:
    print("+18 tá liberado.")

print("*"*60)
# Exercício 31 - pag: 111 - Estrutura de condição if

print("Digite: #1 p/ carne ou #2 p/ massas?")
menu = input("> ")

if menu == "1":
    print("Digite 1. para 'uma carne'")
    print("Digite 2. para 'duas carnes'")

    refeicao = input("\n> ")
    # print(refeicao)
    if refeicao == "1":
        print("pf marmitinha.")
    elif refeicao == "2":
        print("pf marmitão.")

elif menu == "2":
    print("1. espaguete")
    print("2. penne")

    refeicao = input("> ")
    # print(refeicao)
    if refeicao == "1":
        print("Digite : #1. bolonhesa ou #2. carbonara.")

        molho = input("\n> ")
        if molho == "1":
            print("espaguete a bolonhesa.")
        elif molho == "2":
            print("espaguete a carbonara.")

    if refeicao == "2":
        print("escolha o molho para o penne: #1. bolonhesa ou #2. quatro queijos.")

        molho = input("> ")
        if molho == "1":
            print("Penne a bolonhesa.")
        elif molho == "2":
            print("Penne aos quatros queijos.")

else:
    print("veggie.")