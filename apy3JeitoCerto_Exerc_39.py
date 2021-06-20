# -- coding utf-8 --
""" Exercício 39 - dicionarios, ah os adoraveis dicionarios - pag: 143 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
# crie um mapeamento entre estados e siglas
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Maryland':'MD',
    'Massachusetts':'MA',
    'Missouri':'MO',
    'North Carolina': 'NC',
    'Georgia': 'GA'
    
}

# crie um conjunto basico de estados e algumas cidades deles
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'MD' : 'Baltimore',
    'MA':'Boston',
    'MO':'Kansas City',    
}

# adicione mais algumas cidades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['CA'] = 'Sacramento'
cities['CA'] = 'Los Angeles'
cities['FL'] = 'Miami'
cities['NC'] = 'Charlotte'
cities['GA'] = 'Augusta'


# imprima algumas cidades
print('-' * 10)
print("NY State has: ", cities['NY']) # O estado de NY tem...
print("OR State has: ", cities['OR'])
print("CA State has: ", cities['CA'])


# imprima alguns estados
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan']) # A abreviatura de Michigan é...
print("Florida's abbreviation is: ", states['Florida'])
print("Florida's abbreviation is: ", states['Florida'])


# faça isso usando o dic state e depois o cities
print('-' * 10) 
print("Michigan has: ", cities[states['Michigan']]) # Michigan tem..
print("Florida has: ", cities[states['Florida']])

# imprima todas as siglas dos estados
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
# imprima cada cidade no estado
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# agora faça ambos ao mesmo tempo
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# com segurança, obtenha uma sigla de um estado que pode nao estar ali
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# obtenha uma cidade com uma valor padrao
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX is: {city}")
