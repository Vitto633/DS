v = [45, -89, 32, -12, 33]

def primeiro_elemento():
  return v[0]

def exibe_negativos():
  negativos = []
  for i in range(len(v)):
    if(v[i] < 0):
      negativos.append(v[i])
      return negativos
    
def soma_elementos():
  return sum(v)

def media_elementos():
  media = sum(v) / len(v)
  return media

def elementos_impares():
  impares = []
  for i in range(len(v)):
    if((v[i] % 2) != 0):
      impares.append(v[i])
  return impares

def exibe_extremos():
  extremos = []
  extremos.append(v[0])
  ultimo = len(v)
  extremos.append(v[ultimo])
  return extremos

def busca(valor):
  for i in range(len(v)):
    if(v[i] == valor): return True
    else: return False
  
def exibe_indice_par():
  contador = 1
  while(contador < len(v)):
    contador += 2
    print(v[contador])

def get_opcoes():
  while True:
    print("------------")
    print("1 - Retorna o Primeiro Elemento")
    print("2 - Exibe Negativos")
    print("3 - Soma Elementos")
    print("4 - Media dos Elementos")
    print("5 - Elementos Impares")
    print("6 - Exibe Extremos")
    print("7 - Exibe Indices Impares")
    print("8 - Busca")
    print("------------")
    opcao = int(input("Digite a opcao > "))
    match (opcao):
      case 1:
        primeiro_elemento()
        break
      case 2:
        exibe_negativos()
        break
      case 3:
        soma_elementos()
        break
      case 4:
        media_elementos()
        break
      case 5:
        elementos_impares()
        break
      case 6:
        exibe_extremos()
        break
      case 7:
        exibe_indice_impar()
        break
      case 8:
        ordena_vetor()
        break
      case _:
        pass