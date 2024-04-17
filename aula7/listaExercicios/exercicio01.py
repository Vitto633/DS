# fazer um procedimento chamado 'preenche_lista(l)' que preencha uma lista passada por parametro ate que seja digitado
#digitado ponto (.).

def preencheLista (vetor):
    isRunning = True
    contador = 0
    while isRunning:
        valor = input(f"Digite o valor que sera atribuido no indice {contador} da lista: ")
        if valor != '.':
            vetor.append(valor)
        else:
            isRunning = False
        contador = contador + 1