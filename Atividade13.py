#Faca um programa que leia a largura e a altura de uma parede e calcul sua area e a quantidade de tinta, sabendo que cada L de tinta pinta 2 metros quadrados

largura = float(input('largura eh'))
altura = float(input('altura eh'))

area = largura * altura
areapintada = area/2

print('Sua area eh {}, e sao necessarios {} litros'.format(area,areapintada))