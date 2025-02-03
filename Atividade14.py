#Faca um algoritmo que leia o preco de um produto e o mostre com 5% de desconto

preco = float(input('Qual o preco do produto?'))

desconto = 5/100

preconovo = preco * desconto
precocdesconto = preco - preconovo

print('O preco com desconto eh {}'.format(precocdesconto))