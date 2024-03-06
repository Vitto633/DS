
# x = 1
# while x <= 10:
#     print(x)
#     x = x + 1
#     if x == 5:
#         break
# else:
#     print("Isso será executado caso o laço não seja interrompido")

x = 1
while x <= 10:
    opcao = input("Digite o nome:")
    while opcao != "edson":
        opcao = input("Digite o nome: ")
        x = x + 1
        continue
    print("Agora acertou!")

else:
    print("Será executado caso o laço não seja interrompido.")