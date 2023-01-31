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

O resultado desse algoritmo é salvo em um arquivo Excel!

A partir dessa extração é possível fazer diversos filtros e análises usando, por exemplo, a biblioteca Pandas. Alguns exemplo que podem ser obtidos: *Top 5 de menores preços, Top 10 de mais avaliados, Quais os produtos que possuem os maiores descontos e assim por diante*. Porém, o escopo desse projeto se limita no método de raspagem da API e obter as informações acima.

Neste repositório há um exemplo de planilha excel com o resultado da raspagem. É importante destacar que o arquivo, quando salvo, grava a data, hora e minuto da extração.

# Bibliotecas Utilizadas
- [requests](https://requests.readthedocs.io/en/latest/)
- [json](https://docs.python.org/pt-br/3/library/json.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [tqdm](https://tqdm.github.io/)
- [pandas](https://pandas.pydata.org/)

# Autor
Rogerio Vidal de Siqueira

<a href="https://www.linkedin.com/in/rogerio-vidal-de-siqueira-9478aa136/" target="_blank" rel="noopener noreferrer">Meu Linkdin</a>


