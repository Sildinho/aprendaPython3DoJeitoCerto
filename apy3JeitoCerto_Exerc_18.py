# -- coding utf-8 --
""" Exercício 18 - um bom programa inicial - pag: 63 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
# usando uma função com def
# esse aqui é como seus scripts com argv
def print_two(*args):
    arg1, arg2, = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, aquele *args é desnecessario, podemos simplismente fazer isso
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# essa recebe apenas um argumento
def print_one(arg1):
    print(f"arg1: {arg1}")

# esse nao recebe argunto nenhum
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()