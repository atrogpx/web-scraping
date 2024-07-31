from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
response = requests.get(website)
content = response.text
soup = BeautifulSoup(content, 'lxml')

hrefs = []

pages = soup.find_all('li', class_='page-item')
last_page = int(pages[-2].text)

for page_num in range(1, last_page+1)[:3]:

    response = requests.get(f'{website}?page={page_num}')
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    scripts_list = soup.find('ul', class_='scripts-list')
    anchor_elements = scripts_list.find_all('a', href=True)

    for element in anchor_elements:
        href = element.get('href')
        hrefs.append(f'{root}{href}')

    for href in hrefs:
        try:
            response = requests.get(href)
            content = response.text
            soup = BeautifulSoup(content, 'lxml')
            title = soup.find('h1').get_text()
            script = soup.find('div', class_='full-script')
            with open(f'{title}.txt', 'w') as transcript_file:
                transcript_file.write(script.get_text(separator=' ', strip=True))
        except:
            print('------ Link not working -------')
            print(href)