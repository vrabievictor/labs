#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""
from __future__ import print_function


def decripteaza(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    lista = list(mesaj)
    cif = ord(lista[0])-ord('a')

    for index1 in enumerate(lista):
        car = chr(ord(lista[index1])-cif)
        if car.islower():
            lista[index1] = chr(ord(lista[index1])-cif)
        else:
            car = chr(122 - cif + ord(lista[index1]) - 96)
            if car.islower():
                lista[index1] = car
            else:
                lista[index1] = ' '
    print(lista)


def main():
    """ It's a main fucntion Sherlock"""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)

if __name__ == "__main__":
    main()
