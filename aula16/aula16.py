# Aula 16 - Coletando dados na internet

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
resposta = requests.get(url)

sooup = BeautifulSoup(resposta.text, 'html.parser')
quotes = sooup.find_all('div', class_='quote')

for q in quotes:
    frase = q.find('span', class_='text').text
    autor = q.find('small', class_='author').text

    print(f'{frase} : {autor}')

