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
    
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=LISTA EXERCICIOS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=       
    |                                                                           |
    |   [1] = Função que retorna o primeiro valor do vetor.                     |  
    |   [2] = Procedimento que exibe somente os numeros negativos no vetor.     |
    |   [3] = Função que retorna a soma do vetor.                               |
    |   [4] = Função que retorna a media do vetor.                              |
    |   [5] = Exibe numeros impares do vetor.                                   |
    |   [6] = Exibe primeiro e ultimo elemento do vetor.                        |
    |   [7] = Exibe os elementos dos indices pares.                             |
    |   [8] = Retorna true caso o valor do parametro existir no vetor.          |
    |   [9] = Ordena vetor.                                                     |
    |   [10] = Copia os valores do primeiro vetor no segundo.                   |
    |   [11] = Copia os valores de primerio vetor no segundo so que invertidos. | 
    |   [12] = Ordena o vetor em ordem crescente.                               |
    |   [13] = Ordena o vetor em ordem decrescente.                             |
    |   [14] = Escolha a ordem do vetor.                                        | 
    |   [15] = Separa os pares dos impares.                                     |
    |   [16] = Retorna os elementos do vetor que estão acima da média.          |
    |   [17] = Retorna o maior elemento o vetor.                                | 
    |   [0] = para sair                                                         |
    |                                                                           |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=LISTA EXERCICIOS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """)

    opcao = input("Escolha o exercicio: ")
    while not opcao.isnumeric():
        input("invalido, pressione enter para continuar.")
        opcao = input("Escolha o exercicio: ")

    opcao = int(opcao)

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



