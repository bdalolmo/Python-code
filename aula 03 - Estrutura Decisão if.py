
var_verdade = True

var_false = False

if var_verdade == True:
   print('var_verdade é verdadeiro')
else: print('falso')


a=1
b=2

if a >b:
   print(a,'é maior que ',b)
else: print(a,' não é maior que', b)



print('Menu:\n1 = Escreve Breno\n2 = Escreve Maria\n3 = Escreve Joao ')

opcao = input('Escolha uma opcao ' )

aa=''
bb=''
cc=''

if opcao =='1':
    print('Breno')
elif opcao == '2':
    print('Maria')
elif opcao == '3':
    print('Joao')
else:
    print('Opca invalida')

#print('O que o(a) ', 'aa', 'gosta de fazer? ')


#programa que mostre idade, peso e altura e decide se pode entrar no exercito. para isso ela deva ter mais de 18
#pesar mais ou igual a 60 e ter mais de 1,70


idade=raw(('informe sua idade: '))
peso=input(('Informe seu peso: '))
altura= input(('Informe sua altura: '))

if int(idade) >= 18 and int(peso) >= 60 and float(altura) >=1.70:
    print('Voce esta apto para entrar no exercito')
else:
    print('Voce nao esta apto para entrar no exercito')














