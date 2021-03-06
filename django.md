# Apontamentos - Tutorial Django

- Verificar instalação: `python -m django --version`
- Criando um novo projeto: `django-admin startproject nome_do_projeto` (criado um dir de mesmo nome)
  - Não colocar dentro do document root de um servidor web (/home/nome_do_projeto é uma boa ideia)
  - manage.py é um utilitário de linha de comando para se interagir com o projeto de várias maneiras
- Executando o **servidor de desenvolvimento**: `python manage.py runserver` (possui releitura/recarregamento automático para a maioria dos tipos de edições)
  - Por padrão inicia o IP interna na porta 8000, use `python manage.py runserver localhost:8080` para alterar
- Criando um novo aplicativo: `python manage.py startapp nome_do_aplicativo`
  - aplicação é um pacote com certas convenções, é uma aplicação que faz algo. Um projeto é uma coleção de configurações e apps para um website particular. Um projeto pode conter múltiplos apps. Um app pode estar em múltiplos projetos.
  - um app pode estar em qualquer lugar dentro do Python path (melhor que possa ser importado como um módulo de nível superior dentro do projeto)
- Ao criar uma nova view, mapeia a url dela para que possa ser acessada
- A funço include() referencia outros URLconfs. No colocar $ e sim / no final do expressão anterior. Corta o resto da url e envia para o URLconf incluído. Isso permite apps plug-and-play.
- URl é composta por regex e view (opcionalmente kwargs e name):
  - regex: sintaxe para procurar padrões nas strings das URLs. Percorre a lista para baixo comparando a URL solicitada com todos os padrões até encontrar uma que combine. Não leva em conta o nome do domínio, GET nem POST. São compiladas quando o módulo é carregado pela primeira vez. São rápidas, desde que não muito complexas.
  - view: se encontrar uma URL que combine, executa a função da view, enviando os argumentos: HttpRequest e valores capturados. Capturas simples são enviados como argumentos posicionais e capturas nomeadas como argumentos nomeados.
  - kwargs: argumentos nomeados arbitrários podem ser passadas em um dicionário para a view de destino.
  - name: nomear a URL permite que ela seja referenciada de forma inequívoca de qualquer lugar no Django especialmente nos templates. 
  
  Fonte: https://docs.djangoproject.com/pt-br/1.11/intro/tutorial01/
