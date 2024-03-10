import exercicio01
import exercicio02
import exercicio03
import exercicio04
import exercicio05
import exercicio06
import exercicio07
import exercicio08
import exercicio09
import exercicio10

isRunning = True

while isRunning:
    print("+----LISTA DE EXERCICIOS----+")
    print("|                           |")
    print("|    [1]exercicio01         |")
    print("|    [2]exercicio02         |")
    print("|    [3]exercicio03         |")
    print("|    [4]exercicio04         |")
    print("|    [5]exercicio05         |")
    print("|    [6]exercicio06         |")
    print("|    [7]exercicio07         |")
    print("|    [8]exercicio08         |")
    print("|    [9]exercicio09         |")
    print("|    [10]exercicio10        |")
    print("|    [0]para sair           |")
    print("|                           |")
    print("+----LISTA DE EXERCICIOS----+\n")
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            exercicio01.exercicio01()
            input("Pressione enter para continuar.")
        case 2:
            exercicio02.exercício02()
            input("Pressione enter para continuar.")
        case 3:
            exercicio03.exercicio03()
            input("Pressione enter para continuar.")
        case 4:
            exercicio04.exercicio04()
            input("Pressione enter para continuar.")
        case 5:
            exercicio05.exercicio05()
            input("Pressione enter para continuar.")
        case 6:
            exercicio06.exercicio06()
            input("Pressione enter para continuar.")
        case 7:
            exercicio07.exercicio07()
            input("Pressione enter para continuar.")
        case 8:
            exercicio08.exercicio08(
            input("Pressione enter para continuar."))
        case 9:
            exercicio09.exercicio09()
            input("Pressione enter para continuar.")
        case 10:
            exercicio10.exercicio10()
            input("Pressione enter para continuar.")
        case 0:
            isRunning = False
            print("Programa encerrado.")
        case _:
            print("Opção inválida.")
            input("Pressione enter para continuar.")

