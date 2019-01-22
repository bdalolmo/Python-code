import time
'''
try:
    a = 1200/0
except:
    print("nao pode divisao por 0")
'''

try:
    asdadsfas()

except NameError:
    print("Vc digitou alguma coisa errada")
except zeroDivisionError:
    print("nao pode divisao por 0")


print("abbbbbb")

try:
    a = 1200/0
except Exception as erro:
    print("Aconteceu algum erro: ",erro)



def abre_arquivo():
    try:
        arquivo = open('arquivodido.txt')
        return True
    except Exception as erro:
        print("Aconteceu algum erro: ", erro)
        return False

while not abre_arquivo():
    print('Tentanto abrir arquivo')
    time.sleep(5)

print('Fialmentde abriu o arquivo')

