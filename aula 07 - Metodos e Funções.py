#coding: utf-8

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp


retorno = soma(2,1695)

print(retorno)

#------------

def tem_sete_itens(argumento):
    if len(argumento)==7:
        return True
    else:
        return False

print(tem_sete_itens("oi pessoal"))

if tem_sete_itens("1234567"): #posso passar listas.. dicinarios..conjuntos
    print("Tem 7 letras")
else:
    print("nao tem 7 letras")
































