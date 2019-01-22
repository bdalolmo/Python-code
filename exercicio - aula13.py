#exericio paramentro s API JSON
import requests
import json

def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            print('Pesquisando em pagina: ',i)
            req = requests.get('http://www.omdbapi.com/?s=' + titulo + '&type=movie&page=' + str(i))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
            else:
                print('Fim das paginas')
                break

        except:
            print('Fim das paginas')
            break

            print('Conexou falhou')
    return lista


sair = False
while not sair:
        op=input('PESQUISE filme ou SAIR para fechar: ')

        if op =='sair':
            sair = True
        else:
            lista_filmes = lista_filmes(op)
            print('Filmes encontrado! ', len(lista_filmes))
            for filme in lista_filmes:
                print(filme)







