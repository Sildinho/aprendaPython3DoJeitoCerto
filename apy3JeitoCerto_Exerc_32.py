# -- coding utf-8 --
""" Exercício 32 - loop e listas - pag: 115 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarties']

# esse primeiro tipo de loop for percorre uma lista
for number in the_count:
    print(f"This is count {number}")

print('*'*30)

# mesma coisa que o codigo acima
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

print('*'*30)

# tamebm podemos percorre listas mistas
# perceba que temos que usar um {} uma vez que nao sabemos o que há nela
for i in change:
    print(f"I got {i}")

print('*'*30)

# tambem podemos construir listas, primeiro comece com uma vaziaself.

elements = []

# entao use a função range para fazer a contagem de 0 a 5
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append é uma função que listas entendem
    elements.append(i)

print('*'*30)

# agora podemos imprimi-la tambem.
for i in elements:
    print(f"Elements was: {i}")