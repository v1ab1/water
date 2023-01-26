from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get('https://niagara74.ru/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div[1]/div/div[4]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('div', {'class': 'price-col'}).find('div', {'class': 'price'}).find('span', {'class': 'value'}).text.strip()[0:3])
    single = int(soup.find('div', {'class': 'price-col'}).find('div', {'class': 'old-price'}).find('span', {'class': 'value'}).text.strip()[0:3])
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[2]/form/div[2]/div[1]/div[2]/div[1]/div[1]/label').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    box = int(soup.find('div', {'class': 'reverse-packing'}).find('div', {'class': 'field'}).find('div', {'class': 'price-col'}).find('div', {'class': 'price'}).find('span', {'class': 'value'}).text.strip()[0:3])
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    return [single, double, box]
