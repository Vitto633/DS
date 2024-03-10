def exercício02():
    from datetime import date
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = date.today().year

    if ano_atual - ano_nascimento >= 16:
        print("Você poderá votar este ano.")
    else:
        print("Você não poderá votar este ano.")