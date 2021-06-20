# -- coding utf-8 --
""" Exercício 28 - pratica com booleanos - pag: 103 - livro aprenda python 3 do jeito certo by zed shaw - https://learnpythonthehardway.org/ """
n1 = True and True
print("1.", n1)
n2 = False and True
print("2.", n2)
n3 = 1==1 and 2==1
print("3.", n3)
n4 = "test" == "test"
print("4.", n4)
n5 = 1 == 1 or 2!=1
print("5.", n5)
n6 = True and 1==1
print("6.", n6)
n7 = False and 0!=0
print("7.", n7)
n8 = True or 1==1
print("8.", n8)
n9 = "test"== "testing"
print("9.", n9)
n10 = 1!=0 and 2==1
print("10.", n10)
n11 = "test" != "testing"
print("11.", n11)
n12 = "test" == 1
print("12.", n12)
n13 = not (True and False)
print("13.", n13)
n14 = not (1==1 and 0!=1)
print("14.", n14)
n15 = not (10==1 or 1000==1000)
print("15.", n15)
n16 = not (1!=10 or 3==4)
print("16.", n16)
n17 = not ("testing"=="testing" and "Zed" == "Coll Guy")
print("17.", n17)
n18 = 1==1 and (not ("testing" == 1 or 1 ==0))
print("18.", n18)
n19 = "Chunky" == "bacon" and (not (3==4 or 3==3))
print("19.", n19)
n20 = 3==3 and (not("testing" == "testing" or "Python" == "Fun")) # não entendi. T and F = deveria ser F
print("20.", n20)