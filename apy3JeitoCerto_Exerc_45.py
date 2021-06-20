# -- coding utf-8 --
""" Exercício 45 - voce cria um jogo (You Make a Game) - pag: 191
livro "aprenda python 3 do jeito certo" - zed shaw - https://learnpythonthehardway.org/
"""
from sys import exit
from random import randint

class Cena(object):

    def enter(self):
        print ("Esta cena ainda não está configurada.")
        print ("Crie uma subclasse e implemente enter ().")
        exit(1)


class Quentao(object):

    def __init__(self, cena_mapa):
        self.cena_map = cena_mapa


    def play(self):
        atual_cena = self.cena_mapa.inicio_cena ()
        ultima_cena = self.cena_mapa.proxima_cena ('concluido')
        
        while atual_cena != ultima_cena:
            proxima_cena_nome = atual_cena.enter()
            atual_cena = self.cena_mapa.proxima_cena(proxima_cena_nome)

            # ultima cena
            atual_cena.enter()


class Bebado(Cena):
    
    blablabla = [
        "Eu bebo sim Eu tô vivendo",
        "Tem gente que não bebe",
        "E tá morrendo\n",

        "Eu bebo sim Eu tô vivendo",
        "Tem gente que não bebe",
        "E tá morrendo\n",


        "Tem gente que detesta um pileque",
        "Diz que é coisa de moleque",
        "Cafajeste ou coisa assim\n",

        "Mas essa gente",
        "Quando tá com a cara cheia",
        "Vira chave de cadeia",
        "Esvazia o botequim\n",
        
        "Bebida não faz mal a ninguém",    
        "Bebida não faz mal a ninguém",        
        "Bebida não faz mal a ninguém",
        "Água faz mal à saúde"
    ]
    
    print("Beba maus uma com limão!!")


    def enter(self):
        print(Bebado.blablabla)
        exit(1)


class Meio_da_festa(Cena):

    def enter(self):
        print("""
            "Pra que lado eu vou agora?"
            """)
        
        print("# 1. Pula fogueira?")
        print("# 2. Danca quadrilha")
        print("# 3. Barraca do beijo")
        print("# 4. Mastro de sao joao")
    
        acao = input("\n>  ".lower())
        
        
        if acao == "pula fogueira":
            print(("""
                "Pula a fogueira, iaiá",
                "Pula a fogueira, ioiô",
                "Cuidado para não se queimar",
                "Olha que a fogueira já queimou o meu amor",
                
                "Pula a fogueira, iaiá",
                "Pula a fogueira, ioiô",
                "Cuidado para não se queimar",
                "Olha que a fogueira já queimou o meu amor"
                """))
            
            return 'Bebado'


class Pula_fogueira(Cena):


    def enter(self):
        pass

class Danca_quadrilha(Cena):
    

    def enter(self):
        pass


class Barraca_do_beijo(Cena):

    def enter(self):
        pass


class Mastro_de_sao_joao(Cena):

    def enter(self):
        pass


class Mapa(object):
    
    scenes = {
        'meio_da_festa': Meio_da_festa(), # patio da festa
        'pula_fogueira': Pula_fogueira(),
        'danca_quadrilha': Danca_quadrilha(),
        'barraca_do_beijo': Barraca_do_beijo(),
        'bebado': Bebado(),
        'concluido': Concluido()
    }  

    def __init__(self, inicio_cena):
        pass


    def proxima_cena(self, cena_name):
        pass


    def inicio_cena(self):
        pass


a_mapa = Mapa('fogueira')
a_game = Quentao(a_mapa)
a_game.play()
