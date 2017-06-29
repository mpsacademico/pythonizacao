# codig=UTF-8

'''
Olá, eu sou um módulo. Meu nome é tabuada (pode deixar o .py para lá).

Eu sei que estão precisando de mim quando me chamam. Alguém usa a instrução import seguida pelo meu nome.
É assim que é feito para chamar qualquer módulo por essas bandas.

Quando eu sou importado pela primeira vez algo incrível acontece.
Eu mudo de sobrenome, deixo de ser .py e viro .pyc ou .pyo. Geralmente eu vou morar dentro de um diretório chamado __pycache__.
Dizem que esse processo chama-se compilação. Parece que a compilação faz com que eu chegue mais rápido das próximas vezes que for chamado.

Em seguida, eu sou executado. Se for necessário uma nova execução, é necessário usar um método chamado reload().
'''

resultado = []

def calcular(numero):
	del resultado[:]
	for x in range(0, 11):		
		resultado.append(numero*x)
		
print("tabuada.py diz: - Eu sou um módulo e fui carregado e executado!")