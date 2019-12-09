#tratativa de erros nas funções
#try para tentar
#except para dar o retorno sem travar tudo
#Ex:
try:
	a = 10/0
except Exception as erro:
	print("Erro: ", erro)

#except e colocando o nome específico ex NameError ou genérico como Excepcion.
#Podendo adicionar >except Exception as erro:
# print("mimimi", erro)< para saber onde foi o erro