from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://l-w.ru/catalog/voda/lyuksik_19l/")
    driver.find_element(By.CLASS_NAME, 'fancybox-close-small').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    single = int(soup.find('div', {'class': 'price--current'}).text[0:3])
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[1]/div[2]/button[2]').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('div', {'class': 'price--current'}).text[0:3])
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/div[1]/a').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'head-cart').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/div[2]/button[1]').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    box = int(soup.find('div', {'class': 'item-pack__total'}).find_all('span')[1].text[0:3])
    driver.close()
    return [single, double, box]
