from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

web = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=adc4b13b-d074-4e1c-ac46-9f54aa53072b&pf_rd_r=6Z3BNK326ZH91DJ8XS8G'
path = '/home/atro/Documents/chromedriver'
# options = Options()
# options.add_argument('--headless=new')
# options.add_argument('window-size=1920x1080')
driver_service = Service(path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

driver.maximize_window()

paging_elements_bar = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = paging_elements_bar.find_elements(By.XPATH, './li')
last_page = int(pages[-2].text)
current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:

    # time.sleep(3)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container ')))
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "productListItem")]')))
    
    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container ')
    products = driver.find_elements(By.XPATH, '//li[contains(@class, "productListItem")]')
    for product in products:
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, '//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, '//li[contains(@class, "runtimeLabel")]').text)

    current_page = current_page + 1
    next_button = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
    next_button.click()

driver.quit()

df = pd.DataFrame({'Title': book_title, 'Author': book_author, 'Length': book_length})
df.to_csv('audible_products.csv', index=False)