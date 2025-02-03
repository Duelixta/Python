
#Botar tags nas que vc n usa
#nome = input('Olá qual seu nome')
#print('Prazer {:X^20}, Boa tarde'.format(nome))
n1 = int(input('Me de um numero'))
n2 = int(input('Me de outro numero'))
s = n1 + n2 
sub = n1 - n2
m = n1 * n2
e = n1 ** n2
d = n1/n2 
di = n1//n2

print('Sua soma eh {}\n, a subtracao eh {}\n, a multiplicacao eh {}\n, a exponenciacao eh {:3}\n'.format(s,sub,m,e), end= '\nmacacada\n')
print('Sua divisao eh {:.3f}\n, e sua divisao inteira eh {}\n'.format(d,di))
        