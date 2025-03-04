#Estruturas sequênciais
#IF E ELSE
nome = str(input('Qual seu nome'))
if nome == 'Gustavo': #Aqui não é composta ainda
    print('Que nome bonito!')
else: #Aqui já é composta
    print('Nome de macaco')
print('Bom dia, senhor(a){}'.format(nome))

#Outro exemplo

n1 = float(input('Insira uma nota'))
n2 = float(input('Insira uma nota'))

m2 = (n1 + n2)/2

print('Sua média foi de {}'.format(m2))

if m2 > 5.0:
    print('Você foi aprovado!!')
else:
    print('Reprovado.')