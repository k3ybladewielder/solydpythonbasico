#PREVISAO DO TEMPO EM TEMPO REAL
import requests
import json

Cidade = input("Escreva sua cidade: ")

requisicao = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+Cidade+"&APPID=0353554f941fc710bdae424651edc713")

tempo = json.loads(requisicao.text)
print("Previsão: ", tempo["weather"][0]["main"])
print("Temperatura: ", float(tempo["main"]["temp"]) - 273.15)
