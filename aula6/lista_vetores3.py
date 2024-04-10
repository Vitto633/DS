v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

def ordena_vetor(op, v):
  if((type(op) != str) or (op != 'c'.lower()) or (op != 'd'.lower())):
    return 0
  else:
    if(op == 'c'.lower()):
      if(v == v1):
        vetor_organizado = v1.sort()
        print(vetor_organizado)
      elif(v == v2):
        vetor_organizado = v2.sort()
        print(vetor_organizado)

    if(op == 'd'.lower()):
      if(v == v1):
        vetor_organizado = v1.sort(reverse)
        print(vetor_organizado)
      elif(v == v2):
        vetor_organizado = v2.sort(reverse)
        print(vetor_organizado)
    else:
      pass

def conta_acima_media(v):
  contador = 0
  media = sum(v) / len(v)
  for i in range(len(v)):
    if(v[i] > media):
      contador += 1
  return contador

def maior_elemento(v):
  maior = v[0]
  for valor in v:
    if(valor > maior):
      maior = valor
  return maior

def get_opcoes():
  while True:
    print("------------")
    print("1 - Ordena Vetor")
    print("2 - Separa Pares Impares")
    print("3 - Conta Acima Media")
    print("4 - Maior Elemento")
    print("------------")
    opcao = int(input("Digite a opcao > "))
    match (opcao):
      case 1:
        print("C - Crescente")
        print("D - Decrescente")
        letra = input("")
        if(letra == 'c'.lower()):
          ordena_vetor('c')
        if(letra == 'd'.lower()):
          ordena_vetor('d')
        else: pass
        break
      case 2:
        break
      case 3:
        conta_acima_media()
        break
      case 4:
        maior_elemento()
        break