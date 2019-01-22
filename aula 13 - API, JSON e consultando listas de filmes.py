import requests
import json


def requsicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo+ '&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('erro na conexao')
        return None


def printar_detalhes(filme):
    print('Titulo: ',filme['Title'])

    print()


SAIDA = False

while not SAIDA:

        op=input('Escreva nome do filme ou sair para fechar: ')

        if op== 'SAIR':
            SAIDA=True
            print('Saindo..')
        else:
            filme = requsicao(op)
            if filme['Response'] == 'False':
                print('Filme nao encontrado! ')
            else:
                printar_detalhes(filme)

