# -- coding utf-8 --
""" Exercício 29 - a instrução if - pag: 107 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
people = 210
cats = 60
dogs = 200

# Muitos gatos! O mundo está condenado!
if people < cats:
    print("\nToo many cats! The world is doomed!") # Muitos gatos! O mundo está condenado!
    print("\t\tMuitos gatos! O mundo está condenado!")

# Não há muitos gatos! O mundo está salvo!
if people > cats:
    print("\nNot many cats! The world is saved!") # Não há muitos gatos! O mundo está salvo!
    print("\t\tNão há muitos gatos! O mundo está salvo!")

# O mundo babado!
if people < dogs:
    print("\nThe world is drooled on!") # tudo babado.
    print("\t\ttudo babado.")

# O mundo seco
if people > dogs:
    print("\nThe world is dry!") # tá seco.
    print("\t\ttá seco.")
# (20)
dogs *= 5
# Pessoas são maiores ou iguais aos cães
if people >= dogs:
    print(f"\nPeople {people} > Dogs {dogs}")
    print("\nPeople are greater than or equal to dogs.") # mais gente que cachorro
    print("\t\tmais gente que cachorro")
# Pessoas são menores ou iguais aos cães
if people <= dogs:
    print(f"\nPeople {people} < Dogs {dogs}")
    print("\nPeople are less than or equal to dogs.") # mais cachorro que gente
    print("\t\tmais cachorro que gente")
# tá igual.
if people == dogs:
    print(f"People {people} == Dogs {dogs}")
    print("\nPeople are dogs.") # igual
    print("\t\tigual")
