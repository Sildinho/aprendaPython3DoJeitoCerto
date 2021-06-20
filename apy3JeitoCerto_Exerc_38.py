# -- coding utf-8 --
""" Exercício 38 - fazendo coisas com listas - pag: 137 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.") # Espere, não há 10 coisas nessa lista. Vamos consertar isso.

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} itens now.")

print("There we go: ", stuff) # Lá vamos nós: ['Maçãs', 'Laranjas', 'Corvos', 'Telefone', 'Luz', 'Açúcar', 'Menino', 'Menina', 'Banana', 'Milho']

print("Let's do some things with stuff.") # Vamos fazer algumas coisas com as coisas.

print(stuff[1])
print(stuff[-1]) # eita! que chique
print(stuff.pop())
print(' '.join(stuff)) # o que? legal!
print('#'.join(stuff[3:5])) # show de bola!