from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get('https://chebistok.ru/')
    driver.find_element(By.CLASS_NAME, 'btn--red').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('div', {'class': 'bwsb_price'}).find('span').text.strip())
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'blue_box').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    single = int(soup.find('div', {'class': 'bwsb_price'}).find('span').text.strip())
    box = int(soup.find('div', {'class': 'col-xs-12 col-sm-6 col-md-3 empty19'}).find('div', {'class': 'bwsb_price'}).find('span').text.strip())
    driver.close()
    return [single, double, box]

