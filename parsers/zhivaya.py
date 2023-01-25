from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get('https://живаякапля.рф')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    double = int(soup.find('div', {'class': 'ram-calc__calculation-result'}).text.strip()[0:3]) / 2
    driver.find_element(By.XPATH, '//*[@id="bx_2875157043_891"]/div/table/tbody/tr/td[1]/div/div/div/div[1]/form/div[1]/div[1]/div[2]/button[1]').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    single = int(soup.find('div', {'class': 'ram-calc__calculation-result'}).text.strip()[0:3])
    driver.find_element(By.XPATH, '//*[@id="bx_2875157043_891"]/div/table/tbody/tr/td[1]/div/div/div/div[1]/form/div[1]/div[2]/div[2]/button[1]').click()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    box = int(soup.find('div', {'class': 'ram-calc__calculation-result'}).text.strip()[0:3]) - single
    driver.close()
    return [single, double, box]