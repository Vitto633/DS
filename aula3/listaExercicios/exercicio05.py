def exercicio05():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    valores_ordenados = sorted([valor1, valor2, valor3])

    print("Valores em ordem crescente:", valores_ordenados)