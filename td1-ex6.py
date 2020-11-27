import math
from matplotlib import pyplot


def getNext(x0, a, c, m):
    return ((a * x0 + c) % m)#& ((2**m)-1)



NB_ENTIERS_GENERES = 1000
""" # parametres Java
X0 = 156079716630527
A = 25214903917
C = 11
M = 48
"""
X0 = 3
A = 51
C = 0
M = 101
entiers = [X0]


for i in range(1, NB_ENTIERS_GENERES):
    entiers.append(getNext(entiers[i-1], A, C, M))

x = []
y = []

for i in range(0, len(entiers), 2):
    x.append(entiers[i]/M)
    y.append(entiers[i+1]/M)


pyplot.scatter(x, y, s = 5, marker = 'o')
pyplot.title('test 2D')
pyplot.show()

