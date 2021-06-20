# -- coding utf-8 --
""" Exercício 40 - modulos, classes e objetos - pag: 149  - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """



class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you", # Feliz Aniversário
                   "I don't want to get sued", # Eu não quero ser processado
                   "So I'll stop right there"]) # Então, vou parar por aí

bulls_on_parade = Song(["They rally around tha family", # Eles se unem em torno da família
                        "With pockets full of shells"]) # Com bolsos cheios de conchas

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
