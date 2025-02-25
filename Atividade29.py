#Faca um programa que leia o nome completo de uma pessoa e mostre
#O primeiro e o ultimo nome separadamente

nome = str(input('Qual seu nome'))

nomelista = nome.split()

print(nomelista[0])
print(nomelista[-1]) #-1 eh o ultimo