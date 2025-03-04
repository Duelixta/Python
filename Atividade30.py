#Escreva um programa que faça o computador gerar um numero aleatorio de 0 a 5 e faça com que o usuario tente acertar qual seria esse numero

import random

numero = random.randint(0,5)

tenta = int(input('Adivinhe o numero que o computador pensou'))

if numero == tenta:
    print('Parabéns, você acertou')
else:
    print('Fez o L')
