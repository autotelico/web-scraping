from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.mercadolivre.com.br/samsung-galaxy-a14-5g-128gb-4gb-ram-preto/p/MLB22096077?pdp_filters=deal%3AMLB779362-1#polycard_client=homes-korribanSearchTodayPromotions&searchVariation=MLB22096077&position=2&search_layout=grid&type=product&tracking_id=fb036d98-2de0-4fe8-8dec-fe82b795f68c&c_id=/home/today-promotions-recommendations/element&c_uid=99a5d414-9da0-41c2-8acc-b4d707643352'
html_doc = request.urlopen(url).read()
soup = BeautifulSoup(html_doc, 'html.parser')
valor_em_reais = soup.find_all('span', class_='andes-money-amount__fraction')[1]
valor_em_centavos = soup.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-36')
print(f"{valor_em_reais.string},{valor_em_centavos.string}")