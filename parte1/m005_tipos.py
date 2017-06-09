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

print("Números")

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




