#Criamos uma variável(Espaço na memoria) para recebermos algo do usuário.
#O tipo primitivo, deve ser declarado quando formos utilizar a variavel ou formos ler a mesma
#= é Recebe
#Exemplo: N1=input('Digite o número 1') N2=input('Digite o número 2')
#Atribua mais uma variável para a soma de N1 e N2
#S = N1 + N2
#Mostre na tela
#print('Seu resultado é', S)
#Isso nos mostrará, por exemplo, N1 = 3 N2 = 2, o número 32 e não é esse o objetivo, o mais é usado como concatenação.
#Por isso faremos:

N1 = int(input('Digite N1'))
N2 = int(input('Digite N2'))
S = N1 + N2
print('Seu número é', S)

#Nos tipos primitivos temos 4 variações essenciais.
#Int que significa número inteiro (int) EX: 1,2,3,4,5....
#Floats que significam números reais/de pontos flutuantes (float) EX: 1,0;1,1;1,2;1,3;1,4....
#Booleanos que significam valores lógicos (bool) EX: True,False (Sempre capitalizado).
#Strings que significam carácteres (str) EX: 'Ola','Mundo',''.