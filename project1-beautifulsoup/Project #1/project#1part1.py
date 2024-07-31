from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'

response = requests.get(f'{root}/movies')
content = response.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article')
anchor_elements = box.find_all('a', href=True)

hrefs = []

for element in anchor_elements:
    href = element.get('href')
    hrefs.append(f'{root}{href}')

for href in hrefs:
    response = requests.get(href)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    script = box.find('div', class_='full-script')
    with open(f'{title}.txt', 'w') as transcript_file:
        transcript_file.write(script.get_text(separator=' ', strip=True))
