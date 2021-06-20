# -- coding utf-8 --
""" Exercício 24 - mais pratica - pag: 89 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
print("\nLet's practice everything.") # Vamos praticar tudo.
print('You\'d need to know \'bout escapes with \\ that do:') # Você precisa saber sobre escapes com \ que fazem:
print('\n newlines and \t tabs.') # novas linhas e guias.

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. 
"""# onde não há nenhum.

print("-----------")
print(poem)
print("-----------")

five = 10 - 2 + 3 -6
print(f"This should be five: {five}") # Deve ser cinco: 5


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # chama o def e passa o valor de star_point (10000)

# lembre-se de que essa é uma outra maneira de formatar uma string
print("With a starting point of: {}".format(start_point)) # Com um ponto de partida de: 10000
# é como usar a string f""
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") # Teríamos 5.000.000 grãos, 5.000 potes e 50 caixas.

start_point = start_point / 10 # 1000

print("We can also do that this way:")
formula = secret_formula(start_point) # chama o def e passa o valor de star_point (1000)
# essa é uma maneira facil de aplicar uma lista a uma string de formatação.
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # Teríamos 500.000 grãos, 500 potes e 5 caixas.
