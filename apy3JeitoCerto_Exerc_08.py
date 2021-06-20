# -- coding utf-8 --
""" Exercício 08 - imprimindo, imprimindo - pag: 31 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(not True,  not False,  True,  False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))