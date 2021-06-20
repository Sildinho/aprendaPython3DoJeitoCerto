# -- coding utf-8 --
""" Exercício 42 - é-um, tem-um, objetos e classes - pag: 161 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """

## animal é um objeto (sim, meio confuso) veja o crédito extra.
class Animal(object):
    pass

## cao é um animal
class Dog(Animal):

    def __init__(self, name):
        ## cao tem um nome
        self.name = name

## gato é um animal
class Cat(Animal):

    def __init__(self, name):
        ## gato tem um nome
        self.name = name

# pessoa é um objeto
class Person(object):
    def __init__(self, name):
        ## pessoa tem um nome
        self.name = name

        ## pessoa te-um pet de algum tipo
        self.pet = None

# empregado é uma pessoa
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm, o que é essa mágica estranha?
        super(Employee, self).__init__(name)
        ## empregado tem um salario
        self.salary = salary

## peixe é um objeto
class Fish(object):
    pass

## salmao é um peixe
class Salmon(Fish):
    pass

## linguado é um peixe
class Halibut(Fish):
    pass

## rover é um cao
rover = Dog("Rover")

## satan é um gato
satan = Cat("Satan")

## mary é uma pessoa
mary = Person("Mary")

## mary tem um gato chamdo satan
mary.pet = satan

## frank é empregado e seu salario é 120000
frank = Employee("Frank", 120000)

## rover é o cao de frank
frank.pet = rover

## flipper é um peixe
flipper = Fish()

## cruz é um salmao
crouse = Salmon()

## harry é um lingado
harry = Halibut()