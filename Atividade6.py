
#Faça um programa que leia algo do teclado e mostre o seu tipo primitivo e todas as informações sobre ele

N1 = input('Digite algo')
print(N1.isalnum())
print(N1.isalpha())
print(N1.isupper())
print(N1.islower())
print(N1.isnumeric())
print(N1.isspace())
print(N1.istitle())
print(type(N1))