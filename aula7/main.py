#Insere os elementos na lista diretamente

lista = ["edson", 12, 1.57, True, 34]

print(f"Exibe a posição 1 da lista: L[1] = {lista[1]}")
print(f"Exibe a lista inteira: L = {lista}")

lista[4] = "edson"
print(f"L = {lista}")

lista.insert(3, "edson")
print(lista)

lista.append(22)
print(lista)

lista.pop()
print(lista)

lista.remove("edson")
print(lista)

try:
    lista.remove("sexo")
except:
    print("erro")

texto = "edson".lower()
numeroValoresIguais = lista.count(texto)
print(numeroValoresIguais)

print(len(lista))

valores = [1, 2, 3, 4, "a"]

try:
    print(sum(lista))
except:
    print("ERRO GRAVISSIMO")

list1 = [1, 6, 8]
list2 = [9, 15, 17]
list2 = list2 + list1
list1 = list2 + list1
print(list1)
print(list2)

lista3 = [1, 2 ,3 ]
lista4 = lista3
lista3.append(4)
print(lista3)
print(lista4)

listaOrdenada = [4, 7, 89, 34, 20, 18, 2]

listaOrdenada.sort()
print(listaOrdenada)
listaOrdenada.sort(reverse=True)
print(listaOrdenada)

listaReversa = [10, 4, 23, 4]
listaReversa.reverse()
print(listaReversa)

# o append adiciona um item na lista pessoal olha a diferença do append pra o insert bom pessoal presta atenção e o insert faz
# o que ele insere proessor qual a diferença entt lsta .insert blibliablia quer dizer que no indice 1 eu vou inseir os valores
# então testem ai
# tem quantos argumentos tem zero olha la no metodo olha a assinatura do metodo tem dois paramenros pessoal o append pessoal
# eu e a a marion tamo dispenbsados entao pessoal começa a prestar atenção entt o segunda pergunta o insert tem quandtos
# paramtetros ent]ao não basta você saber quantos paametros pessoal olha a assinatura do metodo o append passa um unico valor
# beleza
# proximo o que o pop faz ele remove ok então pror exemplo esse ele tem um deixa eu lembrar o nome ele tem um parametro defaul
# t enão aparece porr exemplo se eue falar lista.po(0) então se nesse caso ele assume o parametro default op  é pilha coloqueri
# outro outro outro o ultimo que eu inseri mas o python usa essa brecha ai
# ai o não ele revmove seria como se a posição zero fosse ua testem ai o arthur uhu bora arthur arthur bora bil bora
# o append faz o que adiciona o elemento ao ultimo elemento da lista o insert adiiona o elemento pela posicao escolhia se eu
# fosse apagar o 1 ia continuar
# bom o remove ele faz o que ele remove o elemento pela posição o dado por exemplo list.remove(57) então testem ai
# a gente vai chegar ai se então pessoal cadu ta com o jamal jamal boa sorte boa sorte jamal pessoal digitem isso aqui
# lista.remove(30)
# ou uma coisa grave ai você não vai ter problema tem alguns metodos que  eu vou pedir pra você criar pra não ter esse
# tipo de falha pessoal o indice pessoal tem muitas situação que bla bla bla
# quero pegar o elemento entao você pensa assim a lista começa aqui e termina aqui a mas eu queria esse então index 4
# denovo é por ai então ele consegue navegar pela lista ai então aprimeira linhaé isso ai que agente perai deixa eu respirar
# então esse metodo reorna m valor entt é parecido com uma funçaõ entt quando eu dou um append ele adiciona uma valor ele n
# o retorna ele so coloca e qual vai ser o valor 2  depois façam um teste de umindice que não exista lista.index(30)
# psiu o que aconteceu kflçajflçkasdfjlçs
# pode ir proximo o count quantos numeros 22 ele ta encontrando ele vai retornar 2 e se por acaso eu colocar um elemento que
# não existe
# e ai ele erra mas ele não pertence a um objeto sempre o metodo tem um metodo que o antecede lista de cima retorna uma
# quantidade de elementos que e igual s 4 testem isso dai
# não o len vce aplica ele em cima de uma lista se você adiciona um dois elementos entao ele vai pegar o estado atual   elemento q
# usa o for ou usa while quando voc geralmente é len mesmo
#