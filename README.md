# WebScraping da API da Shopee
![GitHub](https://img.shields.io/github/license/rvidals/WebScraping-API-Shopee)

# Sobre o projeto
Pesquisando um pouco sobre Web Scraping, me deparei com um vídeo muito legal no [Youtube]( https://www.youtube.com/watch?v=vU-Z9vCsZpQ), em que o programador desenvolve um algoritmo em Python que consome a API da Shopee e obtém diversas informações de todos os produtos anunciados a partir da pesquisa principal.
Trazendo para a minha realidade e interesse, adaptei o algoritmo para pesquisar camisas da nba e obter as seguintes informações de cada produto anunciado:

  - Nome => name
  - Preço => price
  - Preço antes do desconto => price_before_discount
  - Menor Preço=> price_min
  - Menor preço antes do desconto => price_min_before_discount
  - Maior Preço => price_max
  -  Maior preço antes do desconto => price_max_before_discount
  - Desconto =>  discount
  - Local da loja=> shop_location
  - Id da loja=> shopid
  - Id do item => itemid
  - Histórico de saldo=> historical_sold
  - Estoque => stock 
  - Avaliação => rating_star
  - Link => link
  - Avaliação de 0 estrelas => rating_0
  - Avaliação de 1 estrelas => rating_1
  - Avaliação de 2 estrelas => rating_2
  - Avaliação de 3 estrelas => rating_3
  - Avaliação de 4 estrelas => rating_4
  - Avaliação de 5 estrelas => rating_5

Onde o resultado é salvo em um arquivo Excel. É possível fazer diversos filtros e análises usando a biblioteca pandas e só salvar o resultado da análise. Por exemplo, *Top 5 de menores preços, Top 10 de mais avaliados e assim por diante*. Porém, o escopo desse projeto se limita no método de raspagem da API e obter as informações acima.

Neste repositório há uma planilha excel com o resultado da raspagem. 

# Bibliotecas Utilizadas
- requests
- json
- datetime
- tqdm
- pandas

# Autor
Rogerio Vidal de Siqueira

<a href="https://www.linkedin.com/in/rogerio-vidal-de-siqueira-9478aa136/" target="_blank">Linkdin</a>

[Linkdin](https://www.linkedin.com/in/rogerio-vidal-de-siqueira-9478aa136/){:target="_blank" rel="noopener"}

