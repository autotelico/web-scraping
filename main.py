# Este programa pega o valor original de um produto qualquer do Mercado Livre.
# Basta substituir o valor da variável 'url' com a URL do produto que desejar.
from bs4 import BeautifulSoup
from urllib import request

# URL exemplo:
url = 'https://www.mercadolivre.com.br/moto-g23-dual-sim-128-gb-grafite-4-gb-ram/p/MLB21920944#polycard_client=recommendations_home_navigation-recommendations&reco_backend=machinalis-homes-univb-equivalent-offer&reco_client=home_navigation-recommendations&reco_item_pos=1&reco_backend_type=function&reco_id=0507ac92-dd94-4864-8204-d06b3231f776&wid=MLB3488727537&sid=recos&c_id=/home/navigation-recommendations/element&c_uid=eda19039-ac2a-4eb5-9395-b90ded6f7cf3'
html_doc = request.urlopen(url).read()
soup = BeautifulSoup(html_doc, 'html.parser')
valor_em_reais = soup.find_all('span', class_='andes-money-amount__fraction')[0]
valor_em_centavos = soup.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-36')

# Imprima R$ XXX,XX houver valor em centavos. Se não, imprima só os reais.
print(f"Preco original: {valor_em_reais.string},{valor_em_centavos.string}") if (valor_em_centavos) else print(f"Preco original: {valor_em_reais.string}")
