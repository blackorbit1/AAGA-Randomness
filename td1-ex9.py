

# a * x = b


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

profondeur = len(b) - len(a)
x = []

# on regarde de doite à gauche
for position in range(profondeur-1, -1, -1): # >>>>>> il faudrait surement mettre len(b) à la place de profondeur
    should_be = 0
    actualy_is = b[position]

    retenue = 0
    # on parcourt en diagonale
    for i in range(profondeur):
        bit = 0 if position + i >= len(a) else a[position + i]
        if retenue >=1 and bit == 1 :
            should_be = 0 
            retenue += 1
        else:
            should_be = bit
    if should_be == actualy_is : x.insert(0, actualy_is)


