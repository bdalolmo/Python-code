# encoding: utf-8

'''
Faça um programa que leia a quantidade de pessoas que serao convidadas para uma festa.
apos isso o program irá perguntar o nome de tods as pessoas e colcoar numa lista de convidados
apos isso imprimir todos os nomes da lista
 '''


print('#################################################')
print('Programa de controle de convidados para festa:')
print('#################################################')
qtd = int(input('Qual a quantidade de pessoas que irão a festa?'))
lista_convidados = []



#convidado = input(' Nome do convidado: ')


i=1
while i <= qtd: # for i in range(int(convidado))
    convidado=input(' Coloque o nome do convidado  '+ str(i)+':')
    lista_convidados.append(convidado)
    i += 1

print('Serão ',qtd,' convidados')

print('\nLISTA DE CONVIDADOS')
for convidado in lista_convidados:
    print(convidado)

#print(lista_convidados)