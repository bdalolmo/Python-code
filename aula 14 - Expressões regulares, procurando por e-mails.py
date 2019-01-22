import re
import requests



string_de_teste  ='o gato é bonito'

string_de_teste2 ='o gato, a gata, os gatinhos, o gatão'

string_de_teste3 ='o gato, a gata, os gatinhos, o gatão'



padrao = re.search(r'gat.',string_de_teste) # raw string  . encontra a palavra

padrao = re.search(r'\w\w\w\w',string_de_teste) # qualquer palavra com 4 letras

padrao2 = re.findall(r'gat\w',string_de_teste2) # retorna lista o findall

padrao2 = re.findall(r'gat\w+',string_de_teste2) # retorna lista o findall

padrao3 = re.findall(r'[gat]',string_de_teste3) # retorna lista o findall


if padrao:
    print(padrao.group(),' - padrao encontrado')
else:
    print("padrao nao encontrado")

if padrao2:
    print(padrao2)
else:
    print("padrao nao encontrado")

if padrao3:
    print(padrao3)
else:
    print("padrao nao encontrado")

#print(r"oi pessoal\Segunda linha") # caraxteres especiais deixarem de ser especiais




#--------------- padrao email-------------




string_de_email  ='dsfadsfa@afadfa.com'

padrao_email = re.search(r'[\w-]+@+[\w-]+\.[\w.-]+',string_de_email)


print()
if padrao_email:
    print('E-MAIL: ',padrao_email.group(),' - E-MAIL encontrado')
else:
    print("padrao nao encontrado")


requisicao = requests.get("http://www.fisio2000.com.br/?page_id=16")

padrao_novo_email = re.search(r'[\w-]+@+[\w-]+\.[\w.-]+',requisicao.text)

print()
if padrao_novo_email:
    print('E-MAIL: ',padrao_novo_email.group(),' - E-MAIL encontrado')
else:
    print("padrao nao encontrado")





# TEMA -PROGRAMA COTAÇÃO DO SÓLAR , PREVISAO DO TEMPO - utilizar requisições Piai, expres regulares