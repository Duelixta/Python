#Faca um programa na tela que printe o numero, seu sucessor, e seu predecessor

numero = int(input('Me de um numero\n'))
sucessor = numero + 1
predecessor = numero - 1

print('Seu sucessor eh {}, e seu antecessor eh {}, dado o numero {}.'.format(sucessor,predecessor,numero))