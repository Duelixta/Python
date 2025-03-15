#Escreva um programa que leia a velocidade de um carro, se a velocidade exceder 70kmh, mostre uma mensagem que ele será multado. A multa deve custar 7 reais por km acima do limite


velocidade = float(input("Digite a velocidade do carro (km/h): "))


limite_velocidade = 70

if velocidade > limite_velocidade:
    excesso = velocidade - limite_velocidade
    multa = excesso * 7  
    print(f"Você foi multado! Excedeu o limite em {excesso:.2f} km/h.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Velocidade dentro do limite. Dirija com segurança!")