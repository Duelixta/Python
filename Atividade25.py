#Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

numero = str(input('Me de um numero de 0 a 9999'))

print('O numero {} tem {} milhares, {} centenas,{} dezenas e {} unidades'.format(numero,numero[0],numero[1],numero[2],numero[3]))