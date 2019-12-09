consumer_key = 
consumer_secret = 
access_token = 
access_token_Secret = 

import oauth2
import json
import urllib.parse

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(access_token, access_token_Secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe="")
requisicao = cliente.request("https://api.twitter.com/1.1/search/tweets.json?q='" + query_codificada + "&lang=pt")
decodificar = requisicao[1].decode()
objeto = json.loads(decodificar)

for twit in objeto["statuses"]:
    print(twit["user"]["screen_name"])
    print()
    print(twit["text"])


#pprint.pprint(objeto["statuses"][0]["user"]["screen_name"])
#pprint.pprint(objeto["statuses"][0]["text"])
