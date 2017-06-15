# codig=UTF-8

print("DOCUMENTAÇÃO")

txt = '''
PyDOC - ferramenta de documentação do Python
Usa as DocStrings dos módulos para gerar a documentação

OBS: para usar PyDOC sem PATH no Windows, acrescentar antes dos comandos "python -m"

Comandos Linux:

pydoc ./modulo.py - exibe documentação

pydoc -p 8080 - ver documentação das bibliotecas e módulos no browser

pydoc -g - versão gráfica do PyDOC

help(list) - no interpretador, exibe documentação de list

pydoc -w .\\arquivo.py - gera arquivo HTML com a documentação (colorido)
python -m pydoc -w (nome sem py) > arquivo.html
'''
print(txt)