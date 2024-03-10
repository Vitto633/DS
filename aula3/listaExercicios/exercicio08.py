def exercicio08():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    maior = valor1

    if valor2 > maior:
        maior = valor2
    if valor3 > maior:
        maior = valor3

    print("O maior valor é:", maior)