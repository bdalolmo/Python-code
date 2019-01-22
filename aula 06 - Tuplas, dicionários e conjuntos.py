#coding: utf-8

minha_lista = ['Breno', 'Ana']  # list

minha_tupla = ('Breno', 'Ana')  # tuple

meu_dicionario = {'nome:', 'Breno', 'idade', '40'}  # chave e valor

meu_conjunto = {'Breno', 'Ana'}  # nao tem indice..so chave

print(minha_tupla)
print(minha_tupla[0])

for nome in minha_tupla:
    print(nome)

print('Digite 0 para sair!!!')
nome = 'a'
while nome != '0':
    nome = input('Nome de quem esta na tupla?')

    if nome in minha_tupla:
        print(nome, 'esta em minha tupla')
    else:
        print(nome, 'Nao esta em minha tupla')

print()
print('MEU DICIONARIO')
print(meu_dicionario)

print(type(meu_dicionario))

#print(meu_dicionario['idade'])

print(len(meu_dicionario))

if 'Breno' in meu_dicionario:
    print('Breno esta no dicionario')

meu_dicionario.update('Breno','Joao')

esse_dicionario={'nome:','Julia','idade',30}

print(meu_dicionario)

print()
print()

print('##########    CONJUNTOS   ##################')

print(meu_conjunto)
meu_conjunto.add('Julia')



print(meu_conjunto)



lista = []
tupla = ()
dicionario = {}
conjunto = set()



loucura = [(1,2),(3,4),(5,6),({'João','Maria'},{'Alice'})]

print(loucura)












