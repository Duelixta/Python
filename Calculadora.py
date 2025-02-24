import math

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro: Divisao por zero nao eh permitida."
    return a / b


def menu():
    print("\nCalculadora Simples")
    print("Escolha uma operacao:")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplcacao")
    print("4 - Divisao")
    print("0 - Sair")


def main():
    while True:
        menu()
        try:
            opcao = int(input("\nDigite a opcaoo desejada: "))
        except ValueError:
            print("\nErro: Numeros invalidos")
            continue

        if opcao == 0:
            print("\nCalculadora encerrada.")
            break

        if opcao in [1, 2, 3, 4]:
            try:
                num1 = float(input("Digite o primeiro numero: "))
                num2 = float(input("Digite o segundo numero: "))
            except ValueError:
                print("\nErro: Por favor, insira numeros validos.")
                continue

            if opcao == 1:
                print(f"\nResultado: {soma(num1, num2)}")
            elif opcao == 2:
                print(f"\nResultado: {subtracao(num1, num2)}")
            elif opcao == 3:
                print(f"\nResultado: {multiplicacao(num1, num2)}")
            elif opcao == 4:
                print(f"\nResultado: {divisao(num1, num2)}")
        else:
                        print("\nErro: Opcao invalida.")
            
if __name__ == "__main__": #Executar o main primeiro, n executar em ordem
    main()

