def retornaIndiceElemento(vetor, valor):
    try:
        return vetor.index(valor)
    except:
        return "VALOR NAO ENCONTRADO"
