from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np

url = r"https://t-mobile.com/cell-phones/"
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
device_list = []

for device in soup.find_all('div', class_='upf-productCard__track'):
    brand = device.find('span', class_='upf-productCard__title--brand').text
    model = device.find('h3', class_='upf-productCard__title--model').text
    sku = device.find('meta', itemprop='sku').get('content')
    if brand != '' and model != '' and sku != '':
        device_list.append((brand, model, sku))
    
df = pd.DataFrame(device_list, columns={'Brand': '', 'Model': '', 'SKU': ''})
df.index = np.arange(1, len(df) + 1)# Lists starting with #1
df.to_excel('devices-sku.xlsx', engine='xlsxwriter')
