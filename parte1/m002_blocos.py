# inicio do programa

# codig=UTF-8
print("Blocos:") # instrução
print("Os blocos são delimitados por endentação que deve ser consistente") # instrução
print("Um bloco inicia-se após uma linha que contenha dois pontos (:)") # instrução

'''
Os dois pontos vem depois de:
	- definição de estruturas de controle da linguagem
	- declaração de uma nova estrutura
'''

if 5 > 2 : # estrutura de controle da linguagem
	print("5 > 2 = True") # início do bloco I
	# isto é um comentário dentro do bloco I
	print("5 é maior que 2") # bloco I
	if 5 > 0 : # ecl / bloco I
		print("5 é um número positivo") # bloco II e término de bloco I e II
	
def multiplicador(tabuada, valor): # declaração de uma nova estrutura
	return tabuada * valor # início e término do bloco III
	
print("Tabuada do 5") # instrução
for i in range(11): # estrutura de controle da linguagem
	print("5 X", i, "=", multiplicador(5, i)) # início e término do bloco IV
	
# término do programa