#Strings ocupam em mini espaços de memoria, começando a contagem de zero
#Fatiamento, pegar pedaços de uma string 
frase = 'Macaco'
print(frase[2])

#Limitar cadeia, colocamos: e um numero posterior ate onde queremos que a frase saia

frase2 = 'Sexo'
print(frase2[0:3])

#Saltar de forma ordenada os caracteres

frase3 = 'Compre um cachorro ontem'
print(frase3[2:10:2])

#Caso queira comecar do iniico da frase, nao eh necessario digitar 0:x:z, eh so digitar :x:z

frase4 = 'Macacos unidos strong'
print(frase4[:10:2])

#Caso queira que o programa printe todo a frase, sem ter de estabelecer um numero, eh so x:, sem numero apos os dois pontos