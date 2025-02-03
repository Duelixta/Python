#Desenvolva um programa que leia as notas de um aluno ,calcule e mostre sua media

nome = input('Olá qual seu nome?')
print('Tudo bem?{}'.format(nome))
print('Preciso de 3 de suas notas para calcular a media')
nota1 = float(input('Nota 1'))
nota2 = float(input('Nota 2'))
nota3 = float(input('Nota 3'))

media1 = nota1 + nota2 + nota3
mediafinal = media1/3

print('Sua nota final eh de {}'.format(mediafinal))


