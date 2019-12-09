#Esse site omdb tá bugado
import requests
import json

def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?t=" + titulo + "&type=movie")
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro de conexão")
        return None
def printar_detalhes(filme):
    print("Título: ", filme["Title"])
    print("Ano: ", filme["Year"])
    print("Diretor: ", filme["Director"])
    print("Atores: ", filme["Actors"])
    print("Nota: ", filme["imdbRating"])
    print("")

sair = False
while not sair:
    op = input("Escreva o Título de filme ou SAIR: ")

    if op == "SAIR":
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == "False":
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)


