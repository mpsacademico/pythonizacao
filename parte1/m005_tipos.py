# codig=UTF-8

print("TIPOS")
'''
variável - criada por atribuição e destruída pelo Garbage Colector (quando não há mais referências)
nome de variável é uma referência que pode ser alterada em tempo de execução
regras de nomeação: início: letra ou _ ; resto: (letras, dígitos ou _) sem acentos e espaços - sensitive case

-> simples: números, texto e coleções: lista, tupla, dicionário

Tipos: mutáveis - contéudo da variável pode ser alterado; imutáveis - inverso de mutável

tipos e rotinas comuns estão na forma de builtins - sempre disponíveis em tempo de execução
'''

print("Números") # imutáveis

# tipos numéricos
inteiro = 2 # int - e inteiro longo - limitado pela memória disponível
real = 4.5 # float
complexo = 6 + 5j # complex
print(inteiro)
print(real)
print(complexo)

# conversões
print(int(4.5)) # real para inteiro
print(float(2)) # inteiro para real

# mudanças de base
print(int('10',8))
print(int('10',16))

# operações com números complexos
print("complexo =", complexo)
print("parte real =", complexo.real)
print("parte imaginária =", complexo.imag)
print("conjugado =", complexo.conjugate())

# funções para tipos numéricos
print(abs(-4)) # retorna valor absoluto do número
print(oct(10)) # converte para octal
print(hex(10)) # converte para hexadecimal
print(pow(2, 3)) # eleve um número pelo outro
print(round(4.555555, 2)) # retorna um real com arredondamento especificado

# operadores aritméticos
print(5 + 5) # soma
print(5 - 5) # subtração
print(5 * 5) # multiplicação
print(5 / 5) # divisão (divisão inteira entre inteiros)
print(5 // 5) # divisão inteira, mantém o tipo real se for o caso
print(11 % 2) # módulo: retorna o resto da divisão
print(10 ** 3) # potência
print(16 ** 0.5) # potência com expoente fracionário retorna a raiz
print(-13) # negativo
print(+13) # positivo

# operadores lógicos
print(3 < 6) # menor
print(6 > 3) # maior
print(5 <= 5) # menor ou igual
print(4 >= 3) # maior ou igual
print(8 == 8) # igual
print(1 != 0) # diferente

# operadoes bit-a-bit:
print("<<, >>, &, |, ^, ~")

# --------------------------------------------------------------------

print("Textos") # imutável - cada alteração gera uma nova string

# inicialização - tente adotar um padrão
aspasSimples = 'com aspas simples'
aspasDuplas = "com aspas duplas"
linhasConsecutivas = '''1
inicializa-se com 3 aspas simples
ou com 3 aspas duplas
2'''
print(aspasSimples)
print(aspasDuplas)
print(linhasConsecutivas)

# concatenação
animal = 'gato'
cor = "preto"
print(animal + " é " + cor)

# interpolação - é mais eficiente que concatenação
print('A palavra %s tem %d letras' % (animal, len(animal)))
'''
Símbolos para interpolação:
%s - string
%d - inteiro
%o - octal
%x - hexadecimal
%f - real
%e - real exponencial
%% - sinal de porcentagem
'''
print("Octal = %o, Hexadecimal = %x"%(12, 12)) # conversão automática para outras bases
print("%05d" % (1)) # formatação de números - zeros à esquerda (5 zeros a esquerda do decimal)
print("%.1f" % (45.99)) # formatação de números - casas decimais (1 casa decimal após o ponto)
print('%.1f%%, %.2e' % (6.777, 0.00295))

# interpolação com format - útil em laços de repetição
frase = "{0} - {1} - {2}"
print(frase.format('Eu',"sou","filho de Deus"))
frase = "Hora: {hora: 02d} Minuto: {minuto: 02d}"
print(frase.format(hora=14, minuto=1))
print("Pi =", format(3.14159, '.3e'))

# String como sequência no FOR
for caractere in animal:
	print(caractere)
	
# uso de métodos, pois String são objetos
print(animal.upper())

# consistência nas operações
print(5 * "A")

# fatias (slices) de strings - obtidas por índices em colchete
'''
*posições de uma string:
m a c a c o
0 1 2 3 4 5
*índices para fatiamento:
string[início:fim+1:intervalo]
os parâmetros, se não informados, correspondem à:
 - início: 0
 - fim+1: tamanho do objeto
 - intervalo: 1 (entre caracteres)
'''
s = 'macaco'
print(s[0], s[1], s[2], s[3], s[4], s[5]) # acesso a posições individuais - índice começa em 0
print(s[0:], s[1:], s[2:], s[3:], s[4:], s[5:]) # pega da posição inicial informada até o tamanho do objeto
print(s[0:2], s[1:3], s[2:4], s[3:5], s[4:5], s[5]) # pega da posição inicial informada até o fim informado
print(s[-0], s[-1], s[-2], s[-3], s[-4], s[-5]) # começa do final se forem negativos
print(s[0:5:2]) # 2 é o intervalo entre caracteres que serão selecionados m X c X c
print(s[::-1]) # invertendo a string
print("radar"[::-1]) # não dá muito certo com palíndromos :P

# unicode
texto = "texto"
print(texto, type(texto))

unicode = u'Hüsker Dü'
print(unicode, repr(unicode), type(unicode)) # str

str = unicode.encode('latin1')
print(str, repr(str), type(str)) # bytes

unicode = str.decode('latin1')
print(unicode, repr(unicode), type(unicode)) # str

# módulo string
import string

alfabeto = string.ascii_letters # string com o alfabeto
print(alfabeto)

template = string.Template('$string tem $inteiro anos') # template usa um dicionário para gerar a string
string = template.substitute({'string': 'Joaquim', 'inteiro': 14}) 
print(string)

# strings mutáveis (são menos eficientes, consomem mais memória e CPU) - depreciado?
'''
import UserString
mutavel = UserString.MutableString("pato")
mutavel[0] = "g"
print(mutavel, type(mutavel))
'''

# --------------------------------------------------------------------

print("Listas") # mutável - coleção de dados (objetos) heterogêneos 

# criar nova lista
animais = ['pato', 'ganso']
print(animais[0]) # acessando a primeira posição

# imprimir lista
for animal in animais:
	print(animal)

# troca de elementos (último elemento)
animais[-1] = "cachorro"

# incluir elemento
animais.append("gato")

# remover elemento
animais.remove("pato")

# numeração de elementos
for i, animal in enumerate(animais):
	print(i, "-", animal)

# inverter a lista (a operação é aplicada na lista)
animais.reverse()
print(animais)

# ordenar a lista (a operação é aplicada na lista)
animais.sort()
print(animais)

# fatiamento - assim como de strings
print(animais[1:])


# --------------------------------------------------------------------

print("Tuplas") # imutável - semelhantes as listas

# criar nova tupla 
comida = ("Arroz", "Feijão", "Carne", 20, ["entrada", "prato principal", "sobremesa"]) # dados heterogêneos
convidados = ("eu",) # tupla de um elemento deve conter a vírgula ao final
issoEhUmaTupla = "elemento1", 1 # os parênteses são opcionais
print(type(issoEhUmaTupla))

# imprimir tupla
print(comida)

for c in comida:
	print(c)
	
print(convidados[0])

# qualquer tentativa de alteração das referências do objeto irão gerar erros
#comida[0] = "arroz" # gera erro
comida[4].append("bebida")

# conversões tupla X lista - tuplas são estruturas mais simples, por isso computacionalmente mais eficientes
lista = [1, 2, 3]
print(type(lista))
tupla = ("a", "b", "c")
print(type(tupla))

tupla = tuple(lista) # lista para tupla
print(type(tupla))

lista = list(tupla) # tupla para lista
print(type(lista))

'''
set e frozenset sequências para operações com conjuntos
'''

# --------------------------------------------------------------------

print("Dicionários") # mutável - lista de associações entre chave única (elemento imutável) e valor (elemento mutável) - sem garantias de ordenamento

# criar dicionário
pessoa = {'nome': 'Paulo', 'idade': 22}

# acessar elemento
print(pessoa['nome'])

# adicionar elemento
pessoa['endereco'] = "Rua dos Alfeneiros"

# apagar elemento
del pessoa['idade']

# obter elementos diversos da estrutura de um dicionário
itens = pessoa.items()
chaves = pessoa.keys()
valores = pessoa.values()
print(itens)
print(chaves)
print(valores)

# imprimir dicionário
print(pessoa)
for chave, valor in pessoa.items(): # items() - lista de tuplas de chave e valor
	print(chave, ':', valor) 

# --------------------------------------------------------------------

print("Verdadeiro, Falso e Nulo")
txt = \
'''bool é uma especialização de int
True = 1
False = 0, false (falso), none (nulo - NoneType), '' (string vazia),
	    [] (lista vazia), () (tupla vazia), {} (dicionário vazio),
		quaisquer estruturas com tamanho igual a zero		
'''
print(txt)

print("Operados Lógicos - Booleanos")
txt = '''
and, or, not, is (duas referências para o mesmo objeto), in (item ocorrer em lista)
- particularidades do cálculo:
	0 and 3 = 0 | 0 or 3 = 3
	2 and 3 = 3 | 2 or 3 = 2
- all(), any()
'''
print(txt)