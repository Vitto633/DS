def separaParesImpares(vetor1):
    vetorPar = []
    vetorImpar = []
    vetorSoma = []
    for i in range(len(vetor1)):
        if vetor1[i] %2 == 0:
            vetorPar.append(vetor1[i])
        else:
            vetorImpar.append(vetor1[i])
    vetorSoma = vetorPar + vetorImpar
    print(vetorSoma)

