# -- coding utf-8 --
""" Exercício 14 - prompt e passagem - pag: 47 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.") 
print("I'd like to ask you a few questions.") # pode fazer uma.
print(F"Do you like me {user_name}?") # gosto mais ou menos
likes = input(prompt)

print(f"Where do you live {user_name}?") # moro em osasco.
lives = input(prompt)

print("What kind of computer do you have?") # qual seu pc. um aí.
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# python3 apy3JeitoCerto_Exerc_13.py agua gelo neve