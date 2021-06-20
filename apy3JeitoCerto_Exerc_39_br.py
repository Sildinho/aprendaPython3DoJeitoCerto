# -- coding utf-8 --
""" Exercício 39 - dicionarios, ah os adoraveis dicionarios - pag: 147 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
# crie um mapeamento entre estados e siglas
states = {
    'Amapá': 'AP',
    'Alagoas': 'AL',
    'Ceará ': 'CE',
    'Minas Gerais': 'MG',
    'Paraíba': 'PB',
    'Rio Grande do Sul ': 'RS',
    'Santa Catarina': 'SC',
    'Goiás': 'GO'
}

# crie um conjunto basico de estados e algumas cidades deles
cities = {
    'MG': '	Juiz de Fora',
    'AP': 'Santana',
    'AL': 'Maceió',
    'CE': 'Fortaleza',
    'MG': 'Uberlândia',
    'CE': 'Juazeiro do Norte',
    'AL': 'Maragogi'
}

# adicione mais algumas cidades
cities['AL'] = 'Marechal Deodoro'
cities['AP'] = 'Macapá'
cities['PB'] = 'João Pessoa'
cities['RS'] = 'Bagé'
cities['RS'] = 'Santa Cruz do Sul'
cities['SC'] = 'Criciúma'
cities['SC'] = 'Balneário Camboriú'
cities['SC'] = 'Itajaí'
cities['GO'] = 'Goiânia'
cities['GO'] = 'Itumbiara'


# imprima algumas cidades
print('-' * 10)
print("\nNo estado de MG fica: ", cities['MG'])  # O estado de NY tem...
print("No estado de SC fica: ", cities['SC'])
print("No estado de RS fica: ", cities['RS'])


# imprima alguns estados
print('-' * 10)
print("\nA Sigla de Alagaoas é: ", states['Alagoas'])
print("A Sigla de Goiás é: ", states['Goiás'])


# faça isso usando o dic state e depois o cities
print('-' * 10)
print("\nAmapá têm: ", cities[states['Amapá']])  # Michigan tem..
print("Paraíba têm: ", cities[states['Paraíba']])

# imprima todas as siglas dos estados
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"A abreviação do {state} é: {abbrev}\n")

# imprima cada cidade no estado
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"Em {abbrev} fica a cidade {city}\n")

# agora faça ambos ao mesmo tempo
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"O {state} estado é abreviado: {abbrev}")
    print(f"No estado fica  {cities[abbrev]}\n")

print('-' * 10)
# com segurança, obtenha uma sigla de um estado que pode nao estar ali
state = states.get('Acre')

if not state:
    print("Desculpe, sem Acre.")

# obtenha uma cidade com uma valor padrao
city = cities.get('AC', 'Não existe.')
print(f"A cidade para o estado 'AC' é: {city}\N")
