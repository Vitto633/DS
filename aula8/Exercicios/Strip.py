# Imagine que você está desenvolvendo um sistema que precisa processar nomes de usuários que são
# inseridos manualmente. Às vezes, os usuários podem acidentalmente adicionar espaços extras no início ou
# no final dos nomes. Sua tarefa é escrever uma função que limpe esses espaços e retorne o nome limpo.
#
# Instruções:
# Escreva uma função chamada limpar_nome que:
#
# Aceite um parâmetro: nome, que é uma string.
# Utilize o método strip() para remover espaços extras no início e no final da string.
# Retorne a string limpa.
# Teste sua função com as seguintes entradas:
#
# " João "
# " Maria"
# "Carlos "
# " Ana Clara "
# Imprima os resultados dos testes para verificar se a função está funcionando corretamente.

joao = "              João "
maria = " Maria"
carlos = "Carlos "
ana = " Ana Clara "

def limpar_nome(nome):
    return nome.strip()

print(limpar_nome(joao))
