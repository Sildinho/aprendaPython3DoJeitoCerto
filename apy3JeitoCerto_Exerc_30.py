# -- coding utf-8 --
""" Exercício 30 - else & if - pag: 109 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
# 3! = 3*2*1 = 6 possibilidades.
people = 41
cars = 40
trucks = 42

if cars > people:
    print("We should take the cars.") # pra que tantos carros. ?!    
elif cars < people:
    print("We should not take the cars.") # Não devemos ter mais carros.  
else:
    print("We can't decide.") # Não podemos decidir.   

if trucks > cars:
    print("That's too many trucks.") # Muitos caminhões.   
elif trucks < cars:
    print("Maybe we could take the trucks.") # Talvez pudéssemos levar os caminhões.   
else:
    print("We still can't decide.") # Ainda não conseguimos decidir.  

if people > trucks:
    print("Alright, let's just take the trucks.") # Tudo bem, vamos pegar os caminhões.    
else:
    print("Fine, let's stay home then.") # Tudo bem, vamos ficar em casa então.   