def exercicio07():
    numero_lados = int(input("Digite o número de lados do polígono: "))
    medida_lado = float(input("Digite a medida do lado em cm: "))

    if numero_lados < 3:
        print("Não é um polígono.")
    elif numero_lados == 3:
        print("Triângulo")
        # Fórmula para área de um triângulo equilátero
        area = (medida_lado ** 2 * (3 ** 0.5)) / 4
        print("Área:", area)
    elif numero_lados == 4:
        print("Quadrado")
        # Fórmula para área de um quadrado
        area = medida_lado ** 2
        print("Área:", area)
    elif numero_lados == 5:
        print("Pentágono")
        # Fórmula para área de um pentágono regular
        apotema = medida_lado / (2 * (5 ** 0.5))
        area = 5 / 2 * medida_lado * apotema
        print("Área:", area)
    else:
        print("Polígono não identificado.")
