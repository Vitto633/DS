c = 1
i = 0

n = int(input("Digite o valor: "))

while n>c:
    if n%2 == 0:
        i = i + 1
    c = c + 1

if i == 1:
    print("O número é primo ")
else:
    print("O número não é primo")