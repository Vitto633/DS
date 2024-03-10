def exercicio10():
    angulo1 = float(input("Digite o primeiro ângulo: "))
    angulo2 = float(input("Digite o segundo ângulo: "))
    angulo3 = float(input("Digite o terceiro ângulo: "))

    if angulo1 + angulo2 + angulo3 == 180:
        if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
            print("Triângulo acutângulo.")
        elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            print("Triângulo retângulo.")
        else:
            print("Triângulo obtusângulo.")
    else:
        print("Valores inválidos para os ângulos de um triângulo.")