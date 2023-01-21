from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get('https://niagara74.ru/#')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('div', {'class': 'price-col'}).find('div', {'class': 'price'}).find('span', {'class': 'value'}).text.strip()[0:3])
    single = int(soup.find('div', {'class': 'price-col'}).find('div', {'class': 'old-price'}).find('span', {'class': 'value'}).text.strip()[0:3])
    driver.find_element(By.XPATH, '//*[@id="reverse-good-control"]/div[1]/div[1]/label/span').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    box = int(soup.find('div', {'class': 'reverse-packing'}).find('div', {'class': 'field'}).find('div', {'class': 'price-col'}).find('div', {'class': 'price'}).find('span', {'class': 'value'}).text.strip()[0:3])
    driver.close()
    return [single, double, box]

print(parser())