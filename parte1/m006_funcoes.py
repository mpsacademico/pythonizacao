# codig=UTF-8

print("FUNÇÕES") # bloco de código identificado por nome que pode receber parâmetros predeterminados

def nome_da_funcao(parametro1, parametro2 = 'valor_default'): # def - palavra reservada para definir funções
	'''DocString
	Documentação da função: função, parâmetros etc.
		parametro1 - obrigatório
		parametro2 - opcional (valor_default será assumido se não informado)
	'''
	# bloco de código
	print(parametro1)
	print(parametro2)
	return "retorno" # pode ou não retornar um objeto
	
print(nome_da_funcao("parametro1", "parametro2")) # chamada de função com todos os parâmetros informados e uso do retorno

retornado = nome_da_funcao(1, 2) # sem distinção de tipos dos argumentos passados
print(retornado)

#nome_da_funcao() # parametro1 é obrigatório (por não possuir valor default)
nome_da_funcao("primeiro_parametro_apenas") # o valor padrão do parametro2 é assumido quando não informado


# funções possuem namespace próprio - escopo local que ofusca o global
num1 = 10 # variável de escopo global
def soma(num1, num2, num3 = 0):
	return num1 + num2 + num3 # variáveis de escopo local - ofuscam o global (usar global)
	
resultado = soma(5, 6) # valores default devem vir por último
print(resultado)


# parâmetros passados são recebidos pela função em listas e/ou dicionários
def funcao(*args, **kargs):	
	print(args)  # sem identificador: lista
	print(kargs) # com identificador: dicionário
	
funcao()
funcao(1, 2, 3)
funcao(param4 = 4, param5 = 5) # a ordem não importa entre os parâmetros com identificador
funcao(1, 2, 3, param4 = 4, param5 = 5) # parâmetros com identificador devem vir por último

# OBS:decoradores podem alterar as propriedades das funções