def compte_voyelles(chaine):
    nbr_voyelle=0
    for char in chaine:
        if char in "aeiouyAEIOUYéèàêôù":
           nbr_voyelle = nbr_voyelle+1
    return nbr_voyelle
chaine = input('Enter any string: ')
print('nobre de voyelle =',compte_voyelles(chaine))