from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Firefox()
driver.get("https://xn--80aaepkoi5a5le.xn--p1ai/catalog/water/water_drinking_zhivaya_kaplya_19l/?oid=1026")
soup = BeautifulSoup(driver.page_source, 'html.parser')
found = soup.findAll(class_='price_value')
print(found[0].text.strip())
driver.close()