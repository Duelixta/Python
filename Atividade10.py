#Faca um programa que leia um valor em metros e converta para centimetros e milimetros

metros = float(input('Me de um valor em metros'))

centimetros = metros*100
milimetros = metros*1000

print('Voce tem {} centimetros e {} milimetros.'.format(centimetros,milimetros))