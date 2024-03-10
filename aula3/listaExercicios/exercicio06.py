def exercicio06():
    altura = float(input("Digite a altura da pessoa: "))
    sexo = int(input("Digite o sexo (1 para feminino, 2 para masculino): "))

    if sexo == 1:
        peso_ideal = 62.1 * altura - 44.7
        print("O peso ideal para uma mulher com altura", altura, "é:", peso_ideal)
    elif sexo == 2:
        peso_ideal = 72 * altura - 58
        print("O peso ideal para um homem com altura", altura, "é:", peso_ideal)
    else:
        print("Sexo inválido.")