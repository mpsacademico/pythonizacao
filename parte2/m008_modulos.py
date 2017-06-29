# codig=UTF-8

print("MÓDULOS")
'''
- arquivos fonte que podem ser importados
- reaproveitamento e facilidade de manutenção

Primeira importação de um módulo:
- é localizado pelo interpretador usando o PYTHONPATH (sys.path) - lista de diretórios começando pelo do script principal
- compilado e armazenado em arquivo .pyc ou .pyo no diretório __pycache__
- executado (próximas vezes necessita de reload())

São objetos Singleton - uma instância na memória disponível globalmente

if __name__ == "__main__": - VERDADEIRO no módulo principal

'''
# CARREGAMENTO DE MÓDULOS 

# importa absoluta - import MÓDULO (módulo - nome do arquivo Python sem extensão)
import modulo_exemplo_1
print(modulo_exemplo_1.variavel) # a identificação do módulo evita ofuscamentos de variáveis e funções
print(modulo_exemplo_1.funcao())

# importação relativa - from MÓDULO import ESTRUTURA (estrutura = variável, função etc.)
from modulo_exemplo_2 import * # asterisco importa tudo que está definido no módulo
'''
from modulo_exemplo_2 import variavel
from modulo_exemplo_2 import funcao
'''
print(variavel)
print(funcao())

# namespace e DocStrings próprios
import tabuada
print(tabuada.resultado)
tabuada.calcular(5)
print(tabuada.resultado)
tabuada.calcular(6)
print(tabuada.resultado)

# exemplos de módulos nativos do Python
import sys # este módulo provê acesso a algumas variáveis usadas ou mantidas pelo interpretador e funções que interagem fortemente com o interpretador

from pprint import pprint

sys.exit() # para a execução do programa Python
print(sys.path) # uma lista de strings que especificam os caminhos para os módulos
#pprint(sys.path)