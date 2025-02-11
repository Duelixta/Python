#Faca um programa que leia o comprimento do cateto oposto e adjacente e calcuile a hipotenusa
import math
from math import sqrt

co = float(input('Me de o cateto oposto'))
ca = float(input('Me de o cateto adjascente'))

co1= pow(co,2)
ca1= pow(ca,2)

hipotenusa = co1 + ca1


print('o cateto oposto mede {}, o adjacente mede {}, logo , sua hipotenusa sera {}'.format(co,ca,math.sqrt(hipotenusa)))