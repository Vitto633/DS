def acimaDaMedia(vetor):
    acimaDaMedia = 0
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma/len(vetor)
    for x in range(len(vetor)):
        if vetor[x] > media:
            acimaDaMedia += 1
    return acimaDaMedia
