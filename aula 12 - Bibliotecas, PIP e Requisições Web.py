import sys
import time
import requests

cabecalho = {'User-agent': 'Windows 12','Referer': 'https://google.com'}

meus_cookies = {'ultima-visita':'14/01/2022'}

dados = {'username': 'bdalolmo',
         'password': 'stevepoa7777'}

texto = None
try:
    requisicao = requests.get('https://putsreq.com/9MvTvq26uyohQjwf0Gsm',
                              headers=cabecalho,
                              cookies=meus_cookies,
                              data=dados)
    texto = requisicao.text
except Exception as e:
    print("Requisição de erro", e)

print(texto)
#print(requisicao)

#print(type(requisicao))

#print(requisicao.status_code)





























