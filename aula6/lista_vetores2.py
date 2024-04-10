v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

def copia_vetor():
  for i in range(len(v1)):
    v2 = v1.copy()

def inverte_vetor():
  v2 = v1.reverse()

def ordena_vetor_crescente():
  while True:
    op = int(input("Vetor 1 ou 2: "))
    if(op == 2):
      vetor_organizado = v2.sort()
      print(vetor_organizado)
    if(op == 1):
      vetor_organizado = v1.sort()
      print(vetor_organizado)
    else:
      pass

def ordena_vetor_decrescente():
  while True:
    op = int(input("Vetor 1 ou 2: "))
    if(op == 2):
      vetor_organizado = v2.sort(reverse)
      print(vetor_organizado)
    if(op == 1):
      vetor_organizado = v1.sort(reverse)
      print(vetor_organizado)
    else:
      pass

def get_opcoes():
  while True:
    print("------------")
    print("1 - Copia Vetor")
    print("2 - Inverte Vetor")
    print("3 - Ordena Vetor Crescente")
    print("4 - Ordena Vetor Decrescente")
    print("------------")
    opcao = int(input("Digite a opcao > "))
    match (opcao):
      case 1:
        copia_vetor()
        break
      case 2:
        inverte_vetor()
        break
      case 3:
        ordena_vetor_crescente()
        break
      case 4:
        ordena_vetor_decrescente()
        break
      case _:
        pass