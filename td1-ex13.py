import math
from matplotlib import pyplot
import random


def getNext(x0, a, c, m):
    return (a * x0 + c) & ((2**m)-1)



NB_ENTIERS_GENERES = 1000
# parametres Java
X0 = 156079716630527
A = 25214903917
C = 11
M = 48
entiers = [X0]

class Rand48(object):
    def __init__(self, seed, a=25214903917, c=11, m=48):
        self.n = seed
        self.a = a
        self.c = c
        self.m = m
        self.bit_index = 0
        self.number = []
    def srand(self, seed):
        self.n = (seed << 16) + 0x330e
    def next(self):
        self.n = (self.a * self.n + self.c) & ((2**self.m)-1)
        return self.n
    def bit_suivant(self):
        if self.number == [] or self.bit_index == 48:
            self.bit_index = 0
            self.number = []
            self.next()
            for i in range(48):
                self.number.append((self.n >> i) & 1)
        self.bit_index = self.bit_index + 1
        return self.number.pop()
    def get_number(self, max):
        nb_bits = math.ceil(math.log2(max))
        res_bits = ""
        for _ in range(nb_bits):
            res_bits += str(self.bit_suivant())
        res = int(res_bits, 2)
        if res <= max : return res
        else : return self.get_number(max)



bits = []

NB_BITS = 1000000
probability = 1
total = 0
alea = Rand48(156079716630527)
for i in range(NB_BITS):
    bits.append(alea.bit_suivant())

possible_index = [i for i in range(NB_BITS)]
nb_1_to_add = NB_BITS * probability - NB_BITS * 0.5

while nb_1_to_add != 0 and len(possible_index) > 0:
    tmp = int(random.random() * (len(possible_index)-1))
    i = possible_index.pop(tmp)
       
    if nb_1_to_add > 0 and bits[i] == 0:
        bits[i] = 1
        nb_1_to_add -= 1
    elif nb_1_to_add < 0 and bits[i] == 1:
        bits[i] = 0
        nb_1_to_add += 1


for i in range(NB_BITS):
    total += bits[i]

print(total/NB_BITS)


"""
for i in range(1, NB_ENTIERS_GENERES):
    entiers.append(getNext(entiers[i-1], A, C, M))

print(entiers)

"""