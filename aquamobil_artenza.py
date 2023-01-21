from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-artenza-19-l-oborotnaya-tara.html")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('span', {'class': 'js-inprice'}).text.strip())
    driver.find_element(By.CLASS_NAME, 'good__minus').click()
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, 'closebut')[4].click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    single = int(soup.find('span', {'class': 'js-inprice'}).text.strip())  
    driver.close()
    return [single, double, '-']