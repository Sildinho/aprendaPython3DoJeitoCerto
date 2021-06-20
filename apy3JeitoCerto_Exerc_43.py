# -- coding utf-8 --
""" Exercício 43 - basico de analise e design orientados a objetos - pag: 167 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """

"""
“Os alienígenas invadiram uma nave espacial e nosso herói precisa percorrer por um labirinto de salas
desmoronando para poder escapar em uma cápsula e ir para o planeta abaixo. O jogo será 
parecido com um Zork ou Adventure, com saídas de texto e modos divertidos de morrer. ele
terá um mecanis que executa um mapa cheio de salas ou cenas. Cada sala imprimirá
sua própria descrição quando o jogador entrar e informará ao mecanismo qual executar em seguida no mapa.”
"""
from sys import exit
from random import randint
from textwrap import dedent
class Scene (object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

# motor
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.oppening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            # ultima cena
            current_scene.enter()


class Death(Scene):

    # gracejos em quadrinhos são as discussoes durante brigas ou algo do tipo. Ex. um personagem chega pro outro e diz; "voce é um bufão. minha ira cairá sobre ti." kkkkkkkkkkkkk
    quips = [
        "Você morreu. Você meio que é péssimo nisso.",
        "Sua mãe ficaria orgulhosa ... se ela fosse mais inteligente.",
        "Tal um usuário.",
        "Tenho um cachorrinho que é melhor nisso.",
        "Você é pior do que as piadas do seu pai."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
                Os Gothons do Planeta Percal # 25 invadiram sua nave e
                destruiu toda a sua tripulação. Você é o último sobrevivente
                membro e sua última missão é conseguir a destruição de nêutrons
                bomba do Arsenal de Armas, coloque-a na ponte e
                explodir a nave depois de entrar em um pod de fuga.\n
                Você está correndo pelo corredor central para as armas
                Arsenal quando um Gothon salta, pele escamosa vermelha, suja escura
                dentes e fantasia de palhaço maligno fluindo em torno de seu ódio
                corpo cheio. Ele está bloqueando a porta do Arsenal e
                prestes a puxar uma arma para explodir você.
                """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                    Rápido no empate, você puxa seu blaster e atira
                    no Gothon. Sua fantasia de palhaço está fluindo e
                    movendo-se em torno de seu corpo, o que prejudica seu objetivo.
                    Seu laser atinge sua fantasia, mas não o acerta completamente.
                    Isso arruina completamente a fantasia nova de sua mãe
                    comprou-o, o que o fez ficar louco de raiva
                    e explodi-lo repetidamente na cara até que você esteja
                    morto. Então ele come você.                         
                    """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                        Como um boxeador de classe mundial, você se esquiva, tece, escorrega e
                        deslize para a direita enquanto o blaster do Gothon aciona um laser
                        passando por sua cabeça. No meio de sua esquiva engenhosa
                        seu pé escorrega e você bate com a cabeça no metal
                        parede e desmaiar. Você acorda logo depois apenas para
                        morra enquanto o Gothon pisa em sua cabeça e te devora.
                        """))
            return 'death'

        elif action == "tell a joke!":
            print(dedent("""
                        Lucky for you they made you learn Gothon insults in
                        the academy. You tell the one Gothon joke you know:
                        Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                        fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                        not to laugh, then busts out laughing and can't move.
                        While he's laughing you run up and shoot him square in
                        the head putting him down, then jump through the
                        Weapon Armory door.                        
                        """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                    Você faz uma rolagem de mergulho no Arsenal de Armas, agacha e examina
                    a sala para mais Gothons que podem estar se escondendo. Está morto
                    quieto, muito quieto. Você se levanta e corre para o outro lado do
                    a sala e encontrar a bomba de nêutrons em seu recipiente.
                    Há um bloqueio de teclado na caixa e você precisa do código para
                    tire a bomba. Se você errar o código 10 vezes, então
                    a fechadura fecha para sempre e você não pode pegar a bomba. O
                    o código tem 3 dígitos.
                    """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                        The container clicks open and the seal breaks, letting
                        gas out. You grab the neutron bomb and run as fast as
                        you can to the bridge where you must place it in the
                        right spot.
                    """))
            return 'the_brigde'

        else:
            print(dedent("""
                        The lock buzzes one last time and then you hear a
                        sickening melting sound as the mechanism is fused
                        together. You decide to sit there, and finally the
                        Gothons blow up the ship from their ship and you die.   
                    """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
                    Você explodiu na ponte com a bomba de destruição de nêutrons
                    debaixo do seu braço e surpreenda 5 góticos que estão tentando
                    assuma o controle do navio. Cada um deles tem um ainda mais feio
                    traje de palhaço do que o anterior. Eles não puxaram seus
                    armas ainda, pois eles veem a bomba ativa sob o seu
                    braço e não quero detoná-lo.
                    """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                        Em pânico, você joga a bomba no grupo de góticos
                        e salta para a porta. Assim que você solta um
                        Gothon atira em você bem nas costas, matando você. Como
                        você morre, você vê outro Gothon tentando freneticamente
                        desarme a bomba. Você morre sabendo que eles provavelmente vão
                        explodir quando ele explodir.
                    """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                        Você aponta seu blaster para a bomba debaixo do braço e
                        os góticos levantam as mãos e começam a suar.
                        Você recua até a porta, abre e, em seguida,
                        coloque cuidadosamente a bomba no chão, apontando seu
                        blaster nisso. Você então pula de volta pela porta,
                        aperte o botão de fechar e abra a trava para que o
                        Gothons não podem sair. Agora que a bomba está colocada
                        você corre para a cápsula de escape para sair desta lata.
                        """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
                Você corre pela nave tentando desesperadamente chegar a
                a cápsula de fuga antes que toda a nave exploda. Parece
                como quase nenhum Gothon está no navio, então sua corrida é
                livre de interferências. Você chega à câmara com o
                escape pods, e agora preciso escolher um para pegar. Alguns
                eles podem estar danificados, mas você não tem tempo para olhar.
                Há 5 cápsulas, qual você pega?
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                        Você pula para o pod {guess} e clica no botão de ejeção.
                        O pod escapa para o vazio do espaço, então
                        implode quando o casco se rompe, esmagando seu corpo
                        geléia de geléia.
                    """))
            return 'death'

        else:
            print(dedent("""
                        Você pula para o pod {guess} e clica no botão de ejeção.
                        O pod desliza facilmente para o espaço em direção ao
                        planeta abaixo. Enquanto ele voa para o planeta, você olha
                        de volta e ver sua nave implodir e explodir como um
                        estrela brilhante, destruindo o navio Gothon ao mesmo
                        Tempo. Você ganhou!
                        """))


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def oppening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()