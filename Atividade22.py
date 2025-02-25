frase = '   Macaco come banana   '
print(frase.count('a'))

print(frase.upper().count('A')) #Transformei primeiro a frase para caixa alta, e assim contamos os A's maiusculos

print(len(frase))
print(len(frase.strip()))

frase2 = 'Macaco come banana'
print(frase2.replace('Macaco','Primata')) #O replace nao muda a string, vc cria uma instancia momentanea onde mudamos algo na string
print(frase2[0])

frase3 = frase2.replace('Macaco','Cacetudo')
print(frase3)