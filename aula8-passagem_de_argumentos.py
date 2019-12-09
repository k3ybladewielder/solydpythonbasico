#argumento ZERO é o caminho do arquivo.
#argumento UM é o método
#argumento DOIS é o n1
#argumento TRÊS é o n2

import sys
argumentos = sys.argv

def soma(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2

if argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub(float(argumentos[2]) - float(argumentos[3]))

print(resp)
