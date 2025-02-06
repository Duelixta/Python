#Comando import, importar algo de uma biblioteca
#Colocamos from(nome da biblioteca) import Item da biblioteca para importarmos algo especifico

#Biblioteca MATH, CEIL (Arredonda pra cima) FLOOR(Arredonda pra baixo), TRUNCAR(ELIMINAR DA VIRGULA PRA FRENTE), POW (POTENCIA), SQRT (RAIZ QUADRADA), FACTORIAL(FATORIAIS)
import math
num = int(input('Me de um numero'))
raiz = math.sqrt(num)
print('Seu numero e {}'.format(math.floor(raiz)))