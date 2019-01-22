#exercicio - escrevea uma funçao que recee um objeto de coleção e retorna o valor do maior numero
#nesse coleção. faça outra que retona o menor


print(max(5,6,8,10))


def maior_numero(colecao):
        maior = colecao[0]
        for item in colecao:
            if item > maior:
                maior = item
        return maior


print(maior_numero([1,2,3,5,6,8,10,199]))


def menor_numero(colecao):
    menor = colecao[0]
    for item in colecao:
        if item < menor:
            menor = item
    return menor


print(maior_numero([1, 2, 3, 5, 6, 8, 10, 199]))

print(menor_numero([1, 2, 3, 5, 6, 8, 10, 199]))