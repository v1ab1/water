from selenium import webdriver
from bs4 import BeautifulSoup
def parser():
    driver = webdriver.Firefox()
    driver.get("https://vodalubima.ru/")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    found = soup.findAll(class_='t776__price-value')
    driver.close()
    return(found[0].text.strip())
