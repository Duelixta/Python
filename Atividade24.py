    #Crie um programa que leia um nome completo de uma pessoa, e mostre
#O nome com todas as letras maiusculas

nome = str(input('Qual seu nome?\n'))

print(nome.upper())

#O nome com todas as letras minusculas

nome = str(input('Qual su nombre\n'))

print(nome.lower())

#Quantas letras ao todo sem espaços.

nome = str(input('Whats your name'))

quantidade = len(nome.replace(' ',''))

print(quantidade)

#Quantas letras tem o primeiro nome

nome = str(input('Qual seu nome'))

nome1 = nome.split()

print(len(nome1[0]))
