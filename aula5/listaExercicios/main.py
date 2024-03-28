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
import exercicio11
import exercicio12
import exercicio13
import exercicio15
import exercicio16
import exercicio17

vetor1 = [45, -89, 32, -12, 33]
vetor2 = [41, 72, 39, 4, 35]
vetor3 = [0, 0, 0, 0, 0]

isRunning = True
opcao = 0

while isRunning:
    print("""
    +----LISTA EXERCICIOS----+
    |                        |
    |   [1] = exercicio01    |  
    |   [2] = exercicio02    |
    |   [3] = exercicio03    |
    |   [4] = exercicio04    |
    |   [5] = exercicio05    |
    |   [6] = exercicio06    |
    |   [7] = exercicio07    |
    |   [8] = exercicio08    |
    |   [9] = exercicio09    |
    |   [10] = exercicio10   |
    |   [11] = exercicio11   | 
    |   [12] = exercicio12   |
    |   [13] = exercicio13   |
    |   [14] = exercicio14   | 
    |   [15] = exercicio15   |
    |   [16] = exercicio16   |
    |   [17] = exercicio17   | 
    |   [0] = para sair      |
    |                        |
    +----LISTA EXERCICIOS----+
    """)

    opcao = int(input("Escolha o exercicio: "))

    match(opcao):
        case 1:
            print(exercicio01.primeiroElemento(vetor1))
            input("Pressione enter para continuar.")
        case 2:
            exercicio02.numerosNegativos(vetor1)
            input("Pressione enter para continuar.")
        case 3:
            print(exercicio03.somaVetor(vetor1))
            input("Pressione enter para continuar.")
        case 4:
            print(exercicio04.mediaVetor(vetor1))
            input("Pressione enter para continuar.")
        case 5:
            exercicio05.imparVetor(vetor1)
            input("Pressione enter para continuar.")
        case 6:
            exercicio06.extremidadesVetor(vetor1)
            input("Pressione enter para continuar.")
        case 7:
            exercicio07.indicePar(vetor1)
        case 8:
            print(exercicio08.valorNoVetor(vetor2, vetor3))
            input("Pressione enter para continuar.")
        case 9:
            exercicio09.ordenaVetor(vetor2)
            input("Pressione enter para continuar.")
        case 10:
            exercicio10.copiaVetor(vetor2, vetor3)
            input("Pressione enter para continuar.")
        case 11:
            exercicio11.inverteVetor(vetor2, vetor3)
            input("Pressione enter para continuar.")
        case 12:
            exercicio12.ordenaVetor(vetor2)
            input("Pressione enter para continuar.")
        case 13:
            exercicio13.ordenaVetorDecrescente(vetor2)
            input("Pressione enter para continuar.")
        case 14:
            print("""
            [c] = para crescente
            [d] = para decrescente
            """)
            segundaOpcao = input("Escolha a opcao: ")

            match(segundaOpcao):
                case 'c':
                    exercicio12.ordenaVetor(vetor2)
                    input("Pressione enter para continuar.")
                case 'd':
                    exercicio13.ordenaVetorDecrescente(vetor2)
                    input("Pressione enter para continuar.")
        case 15:
            exercicio15.separaParesImpares(vetor2)
            input("Pressione enter para continuar.")
        case 16:
            print(exercicio16.acimaDaMedia(vetor2))
            input("Pressione enter para continuar.")
        case 17:
            print(exercicio17.maiorValor(vetor2))
            input("Pressione enter para continuar.")
        case 0:
            isRunning = False
        case _:
            print("Valor inválido, favor digitar um exercicio válido")
            input("Pressione enter para continuar.")



