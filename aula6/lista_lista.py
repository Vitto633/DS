import random

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def preenche_lista_automatico():
  for i in range(len(lista)):
    lista[i] = random.randint(1, 10)

def preenche_lista_manual():
  for i in range(len(lista)):
    lista[i] = int(input(f"Digite o valor {i+1}: "))

def exibe_lista():
  for i in range(len(lista)):
    print(lista[i])

def conta_elementos():
  i = len(lista)
  return i

def retorna_indice(elemento):
    try:
        return lista.index(elemento)
    except ValueError:
      return -1

def busca(elemento):
  i = lista.count(elemento)
  if(i == 0):
    return -1
  else:
    return i

def conta_inteiro():
  u=0
  for i in range(len(lista)):
    if(type(lista[i]) == int):
      u += 1
  return u

def get_opcoes():
  while True:
    input("Pressione Espaço ... ")
    print("------------")
    print("1 - Preenche lista")
    print("2 - Exibe lista")
    print("3 - Conta Elementos")
    print("4 - Retorna Indice do Elemento do Parametro")
    print("5 - Busca de Acordo com o Parametro")
    print("6 - Conta a Quantidade de Inteiros")
    print("")
    print("------------") 
    opcao = int(input("Digite a opcao > "))
    match (opcao):
      case 1: 
        print("""
           Escolha 1:
            Automatico
            Manual

        """)
        x = input("Escolha 1: ")
        if(x.lower() == 'automatico'): 
          preenche_lista_automatico()        
        if(x.lower() == 'manual'):
          preenche_lista_manual()
        pass
      
      case 2:
        exibe_lista()
        pass
      case 3:
        print(conta_elementos())
        pass
      case 4:
        x = int(input("Digite o numero para retornar o indice > "))
        print(retorna_indice(x))
        pass
      case 5:
        x = int(input("Digite o numero para retornar a quantidade de elementos"))
        print(busca(x))
        break
      case 6:
        conta_inteiro()
        break 
