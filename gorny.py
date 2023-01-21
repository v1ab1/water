from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def parser():
    driver = webdriver.Firefox()
    driver.get('https://www.74mv.ru/katalog/gornyj-oazis/вода-питьевая-горный-оазис-негазированная-19,0л-detail')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('span', {'class': 'PriceunitPrice'}).text.strip()[0:3])
    return [double, double, '-']