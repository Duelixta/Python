#Faca um algoritmo que leia o salario de alguem com 15% de aumento

salario = float(input('Passa seu salario pa nois'))

porcentagem = 15/100

salariof = salario * porcentagem

salariofinal = salario + salariof

print('Seu salario final eh {}'.format(salariofinal))