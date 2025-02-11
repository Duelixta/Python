#Faca um programa que leia um angulo e mostre  o valor do seu seno cosseno e tangente
import math
ang = int(input('Me de um angulo'))
#Converter p radiandos

rad = math.radians(ang)

sen = math.sin(rad)
coss = math.cos(rad)
tg = math.tan(rad)
print('Seno do angulo {}, eh {}, o cosseno do angulo {},eh {}, e a tg de {}, eh {}'.format(ang,sen,ang,coss,ang,tg))