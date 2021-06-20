# -- coding utf-8 --
# exemplos livro aprenda python 3 do jeito certo - pag: 115 a 121
print("\n")
print("For:\n")
elements = []
for i in range(6):
    print(f"Adding {i} to the list.")
    elements.append(i)



print("\n")
print("*"*60)
# Exercício 32 - pag: 115 - Estrutura de repetição while (w3schools)
print("Break:\n") # pare quando achar
fruits = ["apple", "clementine" , "guava", "orange", "pineapple", "banana", "cherry"]
for x1 in fruits:
    if x1 == "banana":
        break
    print(x1)


print("\n")
print("*"*60)
print("Continue:\n") # pule quando achar.
fruits2 = ["apple", "banana", "cherry", "Grape", "Avocado", "Coconut"]
for x2 in fruits2:
    if x2 == "banana":
        continue
    print(x2)


print("\n")
print("*"*60)
print("Range:\n")
for x3 in range(6):
    print(x3)

print("\n")
print("*"*60)
print("Usando o parâmetro inicial:\n")
for x4 in range(2, 6):
    print(x4)

print("\n")
print("*"*60)
print("Incremente a sequência com 3 (o padrão é 1):\n")
for x5 in range(2, 15, 3):
    print(x5)


print("\n")
print("*"*60)
print("Imprime todos os números de 0 a 5:\n")
for x6 in range(6):
    print(x6)
else:
    print("Finally finished!")

print("\n")
print("*"*60)
print("\nImprime cada adjetivo para cada fruta.")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x7 in adj:
    for y1 in fruits:
        print(x7, y1)