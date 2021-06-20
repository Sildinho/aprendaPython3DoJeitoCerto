# -- coding utf-8 --
""" Exercício 04 - variaveis e nomes - pag: 20 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """

carros = 100 # int
espaco_no_carro = 4.0 # float
motoristas = 30.0 # motoristas
passageiros = 90.0 # passageiros

carros_sem_motorista = carros - motoristas # carro parados
carros_com_motorista = motoristas # carros com motorista
capacidade_de_carona = carros_com_motorista * espaco_no_carro # capacidade de passageiros = 120
media_passageiros_por_carro = passageiros / carros_com_motorista # passageiros por carro = 90

print ("\nexistem", carros, "carros disponíveis.") # carros disponíveis
print ("\nExistem apenas", motoristas, "motoristas disponíveis.") # motoristas disponiveis
print ("\nTeremos", carros_sem_motorista, "carros vazios hoje.\n") # carros vazios hoje
print ("Podemos transportar até", capacidade_de_carona, "caroneiros, hoje.") # pessoas transportadas (motoristas + caronas) hoje
print ("Temos", passageiros, "caroneiros, hoje.") # caroneiros hoje
print ("Precisamos colocar", media_passageiros_por_carro, "em cada carro.\n") #passageiros em cada em cada carroarro

print("***   sublinhado *** "*5)

print('{:s}'.format('\u0332'.join(f"\nPodemos transportar até {capacidade_de_carona} caroneiros, hoje."))) # sublinhado

print ("\u0333".join(f"\nTemos {passageiros} caroneiros, hoje.")) # sublinhado duplo

print ("\u0332".join(f"\nPrecisamos colocar {media_passageiros_por_carro} em cada carro.\n").upper()) #  sublinhado maiusculo