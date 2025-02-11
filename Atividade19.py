#Um profesor quer sortear um aluno, faca um programa que leia 4 nomes e faça um sorteio entre eles

import random

nome1= str(input('Nome de um aluno'))
nome2= str(input('Nome de um aluno'))
nome3= str(input('Nome de um aluno'))
nome4= str(input('Nome de um aluno'))


alunos = [nome1,nome2,nome3,nome4] #Lista com os elementos do sorteio

sorteado = random.choice(alunos)

print(f'o sorteado foi {sorteado}')