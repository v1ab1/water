from selenium import webdriver
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://vlasovkluch.ru/cat/product/item_6.html")
    time.sleep(3)
    driver.refresh()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    found = soup.find(class_='price-inf-info-card-product')
    driver.close()
    arr = [int(found.text.split()[0]), int(found.text.split()[0]), '-']
    return(arr)
