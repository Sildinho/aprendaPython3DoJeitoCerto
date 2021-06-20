# -- coding utf-8 --
""" Exercício 19 - funções e variaveis - pag: 67 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # chamando a função. passando 20 e 30


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # chamando a função. passando 10 e 50

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # chamando a função. passando 30 e 11, substituindo o "amount_of_crackers"

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # chamando a função. passando 10 + 100 e 50 + 1000


