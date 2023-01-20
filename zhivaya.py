from selenium import webdriver
from bs4 import BeautifulSoup
def parser():
    driver = webdriver.Firefox()
    driver.get("https://xn--80aaepkoi5a5le.xn--p1ai/catalog/voda/voda_pitevaya_zhivaya_kaplya_19l/?oid=1137")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    found = soup.findAll(class_='price_value')
    driver.close()
    return(found[0].text.strip())
