from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get('https://voda174.ru/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    single = int(soup.find('div', {'id': 'ca0c88657e994c28b36f01620278fa9b'}).find('div').text[7:10].strip())
    double = int(soup.find('div', {'id': '6c0e3e2de3654cc09e3e185149df24be'}).find('div').find('b').find('span').text[0:3].strip())
    box = int(soup.find('div', {'id': 'f75f5656e56542c78645cf2ff4fe6b05'}).find('div').find('b').text[0:3].strip())
    driver.close()
    return [single, double, box]
