# -- coding utf-8 --
""" Exercício 33 - loops while - pag: 119 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/"""
i = 0
numbers = []

while i < 6:
    print(f"\nNo inicio: {i}")
    numbers.append(i)

    i = i + 1
    print("O numero agora: ", numbers)
    print(f"é atribuito para i: {i}")

print("O numero: ")

for num in numbers:
    print(num)
