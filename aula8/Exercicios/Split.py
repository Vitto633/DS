# Exercício: Separação de Dados de Entrada
# Imagine que você está desenvolvendo um sistema que precisa processar uma lista de palavras que
# são inseridas como uma única string. Sua tarefa é escrever uma função que separe essas palavras em uma
# lista de palavras individuais.
#
# Instruções:
# Escreva uma função chamada separar_palavras que:
#
# Aceite um parâmetro: frase, que é uma string.
# Utilize o método split() para separar a string em uma lista de palavras, considerando espaços como delimitadores.
# Retorne a lista de palavras.
# Teste sua função com as seguintes entradas:
#
# "O rato roeu a roupa do rei de Roma"
# "Aprender Python é muito divertido"
# "Eu gosto de programar"


frase = "O rato roeu a roupa do rei de Roma"


# o split recebe um parametro que é o que você quer separar
def separarFrase(frase):
    return frase.split("")

def juntaFrases():
    print("".join(separarFrase(frase)))

juntaFrases()
