#Crie um programa que leia o nome de uma cidade e veja se seu nome começa com SANTO

cidade = str(input('Qual o nome da sua cidade'))
cidadel = cidade.split()
cidadel2 = cidadel[0]
print('SANTO' in cidadel2)