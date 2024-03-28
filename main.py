from bs4 import BeautifulSoup
from urllib import request

html_doc = request.urlopen('https://beautiful-soup-4.readthedocs.io/en/latest/').read()
soup = BeautifulSoup(html_doc, 'html.parser')
first_h1 = soup.find('h1')
first_h1.string = 'Crazy!! I changed the h1 tag!'
print(first_h1)