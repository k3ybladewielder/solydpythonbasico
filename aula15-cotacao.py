#COTAÇÃO DO DOLLAR EM TEMPO REAL
import requests
import json
import time
import datetime

#PRA FICAR ATUALIZANDO:
while True:
    requisicao = requests.get("https://api.promasters.net.br/cotacao/v1/valores")
    cotacao = json.loads(requisicao.text)

    print("###COTAÇÃO###", datetime.datetime.now())
    print("Dólar: ", cotacao["valores"]["USD"]["valor"])
    print("Euro: ", cotacao["valores"]["EUR"]["valor"])
    print("BTC: ", cotacao["valores"]["BTC"]["valor"])
    time.sleep(60)
