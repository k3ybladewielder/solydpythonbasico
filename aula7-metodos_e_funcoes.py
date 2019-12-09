#Funções são definíveis. EX1:

def tem_5_letras (x):
    if len (x) == 5:
        return "Tem 5 letras"
    if len (x) > 5:
        return "Tem mais de 5 letras"
    if len (x) < 5:
        return "Tem menos de 5 letras"
def tem_10_letras (x):
    if len (x) == 10:
        return "Tem 10 letras"
    if len (x) > 10:
        return "Tem mais de 10 letras"
    if len (x) < 10:
        return "Tem menos de 10 letras"

print(tem_10_letras("aaaaaaaaaaaaaaaaa"))


#EXERCICIO: Escreva uma função que recebe um objeto de coleção (lista, conjunto etc.)
#  e vai retornar o valor do maior e outra o menor número dessa coleção.

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item
def menor (colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item