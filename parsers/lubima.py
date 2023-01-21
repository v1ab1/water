from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get('https://vodalubima.ru/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    single = int(soup.find_all('div', {'class': 't776__price-value'})[0].text.strip())
    double = int(soup.find_all('div', {'class': 't776__descr'})[0].text.strip()[18:21])
    box = int(soup.find_all('div', {'class': 't776__price-value'})[2].text.strip())
    driver.close()
    return [single, double, box]
