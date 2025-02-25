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

#Caso demos print, poderiamos fazer print(frase[9::20]), printariamos do 9 ate o final, pulando 20 em 20 caracteres.

frase5 = 'Macaco mto foda'

#Analise

frase6 = 'Type stuf macaco foda'
len(frase6) #Tamanho, quantos micro espacos precisa na memoria
frase.count('t') #Contar quantas vezes aparece a letra t.
frase.count('t',2,3) #Contar quantas vezes aparece a letra t, de uma posição até a outra.
frase.find('deo') #Quantas vezes ele encontrou a parte DEO, mostrando onde ele começa
frase5.find('Joana') #Como não temos Joana na frase5, ele mostrará o valor -1
'Curso' in frase5 #Isso vai te responder existe CURSO na variavel FRASE5, com SIM OU NAO, o FIND acha a posição do mesmo.
frase5.replace('Macaco','Primata') #Troca uma palavra da string por outra
frase5.upper() #Deixa maisculo
frase5.lower() #Deixa minusculo
frase5.capitalize() #Joga tudo para minusculo, somente a primeira letra fica maiuscula
frase5.title() #Analisa cada palavra na string,baseada nos espaços, e capitaliza todas as palavras nela
frase5.strip() #Remove espaços inuteis
frase5.rstrip() #Ele remove somente os da DIREITA (RIGHT)
frase5.lstrip() #Remove somente os da ESQUERDA (LEFT)
frase.split() #Onde tiver espaços, ele cria uma divisão, indexando novamente as palavras baseadas no espaço
'-'.join(frase) #Gera uma string unica, juntando a string com -
print("""Aqui dá pra printar uma frase muito longa, sem a necessidade de ficarmos recriando print por print, linha por linha, executando coisas passo a passo. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA""")