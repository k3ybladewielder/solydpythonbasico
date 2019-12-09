#regex101, site para montar e testar expressoes regulares
#padrao de email. EX:
#email@dominio.com.br
#Ou seja, [\w\.-]+@[\w\.-]+.\w+\.[\w\.-]+
#Biblioteca para expressoes regulares (padrões):
import requests
import re

requisicao = requests.get("http://lacoxinha.com.br/contato")

padrao = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", requisicao.text)
#r"" antes da string para ficar string crua

if padrao:
    print(padrao) #ponto group para imprimir texto, sem group imprime o objeto
else:
    print("Padrão não encontrado")



#Pesquisar WEB CRAWLER
