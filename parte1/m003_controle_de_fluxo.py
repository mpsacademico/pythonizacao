# codig=UTF-8
print("Controle de Fluxo") # execução condicional de blocos de código

valor = 5
if valor < 6: # parênteses apenas em casos de ambiguidade
	print("Barato")
elif 6 <= valor <= 20:
	print("Médio")
elif 21 <= valor <= 50:
	print("Caro")
else:
	print("Muito Caro")
# ocorrências por estrutura: if = 1, elif = 0 a N e else = 0 a 1 

'''
numero = input("Informe um número para ser avaliado:") # entrada de dados pelo teclado
#print(type(numero)) # a entrada pelo comando input retorna uma string
numero = int(numero)
'''
numero = 1
# se o bloco tiver apenas uma linha, ele pode ser colocado após os dois pontos
if numero >= 0: print("Número Positivo")
else: print("Número Negativo")

# operador ternário retorna um dos dois valores conforme a condição avaliada
# <variável> = <valor1_se_true> if <condição> else <valor_2_se_false>
idade = 18
maioridade = "É maior" if idade >= 18 else "É menor"
print(maioridade, "de idade")
