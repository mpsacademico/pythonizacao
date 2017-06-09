# codig=UTF-8

print("FOR") # repete de forma estática ou dinâmica

animais = ['Cachorro', 'Gato', 'Papagaio'] # o for pode iterar sobre uma coleção (com interador) de forma sequencial
for animal in animais: # a referência animal é atualizada a cada iteração
	print(animal)
else: # executado ao final do laço (exceto com break)
	print("A lista de animais terminou no ELSE")
	
# contando pares: passando para a próxima iteração em caso de ímpar
for numero in range(0, 11, 1):
	if numero % 2 != 0:
		#print(numero, "é ímpar")
		continue # passa para a próxima iteração
	print(numero)
else:
	print("A contagem de pares terminou no ELSE")
	
'''
range(m, n, p) = retorna uma lista de inteiros
 - começa em m
 - menores que n
 - passos de comprimento p
'''

# saldo negativo: parando o laço em caso de valor negativo
saldo = 100
for saque in range(1, 101, 1):
	resto = saldo - saque
	if resto < 0:
		break # interrompe o laço, o ELSE não é executado
	saldo = resto
	print("Saque:", saque, "| Saldo", saldo)
else:
	print("ELSE não é executado, pois o laço sofreu um break")
	
# --------------------------------------------------------------------

print("WHILE") # repete enquanto a codição for verdadeira

idade = 0
while idade < 18:
	escopo = "escopo" # variável definida dentro do while
	idade += 1 # incrementar unitariamente assim
	if idade == 4:
		print(idade, "anos: tomar vacina")
		continue # pula o resto e vai para próxima iteração
	if idade == 15:
		print("Ops! :( ")
		break # interrompe o laço completamente!!!
	print(idade)	
else:
	print("ELSE: Você já é maior de idade | ESCOPOS:", idade, escopo)