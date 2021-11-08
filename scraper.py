import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://www.olx.pt/imoveis/casas-moradias-para-arrendar-vender/moradias-venda/porto/?page='

lista_imoveis = []

for i in range(1, 25):
    response = requests.get(url_base + str(i))
    
    site = BeautifulSoup(response.text, 'html.parser')

    casas = site.findAll('div', attrs={'class': 'offer-wrapper'})
    print('Pagina', i)
    for casa in casas:
        titulo = casa.find('h3', attrs={'class': 'lheight22 margintop5'})
        link = titulo.find('a')
        preco = casa.find('p',attrs={'class': 'price'})

        #real = produto.find('span', attrs={'class': 'price-tag-fraction'})
        #centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

        #print(casa.prettify())
        #print('Título :', titulo.text.strip())
        #print('Link do produto:', link['href'])
        #print('Preço:', preco.text.strip())
        lista_imoveis.append([titulo.text.strip(),preco.text.strip(),link['href']])

        # if (centavos):
        #     print('Preço do produto: R$', real.text + ',' + centavos.text)
        # else:
        #     print('Preço do produto: R$', real.text)

    print('existem ', len(casas))

news = pd.DataFrame(lista_imoveis, columns=['Título', 'Preço', 'Link'])

news.to_excel('casas.xlsx')
