import lista_vetores1
import lista_vetores2
import lista_vetores3
import lista_lista

while True:
  print("Escolha a lista")
  print("0 - Sair")
  print("1 - Lista Vetores 1")
  print("2 - Lista Vetores 2")
  print("3 - Lista Vetores 3")
  print("4 - Lista Listas")
  opcao = int(input(" > "))
  match(opcao):
    case 0:
      exit()
    case 1:
      lista_vetores1.get_opcoes()
      break
    case 2:
      lista_vetores2.get_opcoes()
      break
    case 3:
      lista_vetores3.get_opcoes()
      break
    case 4:
      lista_lista.get_opcoes()
      break
    case _:
      pass
  
