print("Ficha de aptidão")

idade = int(input ("Escreva idade:"))
peso = float(input ("Escreva seu peso:"))
altura = float(input ("Escreva altura:"))

print("\nResultado: ")
if idade >= 18 and peso >= 60 and altura >= 1.70:
    print("Você está apto")
else:
    print("Você não está apto")
