

# a * x = b

a = [1,1,0,1]
b = [1,0,1,1,0,1,1,0]

"""
    1101
   *1110
   -----
    0000
   11010
  110100
+1101000
--------
10110110

4 567
3 456
2 345
1 234
0 123     
-1 012    
-2 -101
"""
if a[0] == 1 and a[1] == 1: # veut dire qu'il y aura forcément une retenue à la fin
    profondeur = len(b) - len(a) 
    largeur = len(b) - 1
else : 
    profondeur = 1 + len(b) - len(a)
    largeur = len(b)

x = []
positions_zeros = []

"""
# on se place au 1er 1
for position in range(largeur-1, -1, -1): 
    if b[position] == 0
"""
retenue = 0
differences_started = False
# on regarde de doite à gauche
for position in range(len(a)-1, len(a)-len(b), -1): # il faut bien prendre len(b) parce que sinon on ratterait le should_be de la derniere retenue
    should_be = 0
    #pas trop sur de cette partie, ça devrait pas etre b[largeur + (position - (len(a)-1)) - 1] ??
    print(">>> " + str(largeur + (position - (len(a)-1)) ) + "    " + str((position - (len(a)-1))))
    actualy_is = b[largeur + (position - (len(a)-1)) ]

    #retenue = 0
    print("=========")
    print(position)
    print(retenue)
    print(actualy_is)
    print("-------")

    """
        1101
       *1110
       -----
        0000
       11010
      110100
    +1101000
    --------
    10110110
    """
    
    if retenue >=1 :
        should_be = 1 
        retenue -= 1
    # on parcourt en diagonale
    for i in range(profondeur):
        bit = 0 if position + i < 0 or position + i >= len(a) or i in positions_zeros else a[position + i]
        
        if should_be == 1 and bit == 1 :
            should_be = 0 
            retenue += 1
        elif retenue >=1 and bit == 1 :
            should_be = 0 
            retenue += 1
        else:
            should_be += bit
        print(str(0 if position + i < 0 or position + i >= len(a) else a[position + i]) + "  " + str(should_be) + "  " + str(retenue))
    if retenue % 2 == 0 and should_be == 0 : 
        should_be = 1
        retenue -= 1
    
    if should_be == actualy_is and differences_started : x.insert(0, actualy_is) # veut dire que pour l'instant il n y a aucune différence avec x = 11..11
    elif should_be == actualy_is : pass
    else : 
        differences_started = True
        x.insert(0, 0) # veut dire qu'il y a un 0 dans x
        positions_zeros.append(len(x) - 1) # il faut prendre en compte ce nouveau 0 dans les prochains should_be
    print("-------")
    print(should_be)
    print(actualy_is)
    print(positions_zeros)

x = []
for i in range(profondeur):
    print(i)
    print(positions_zeros)
    print(x)
    if len(positions_zeros) > 0 and positions_zeros[0] == i:
        positions_zeros.pop()
        x.insert(0,0)
    else :
        x.insert(0,1)
    
print("Res ======")
print(positions_zeros)
print(x)


