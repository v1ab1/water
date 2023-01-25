from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://живаякапля.рф/sale/")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[13]/a').click()
    element = driver.find_element(By.XPATH, '/html/body/div[6]/div[6]/div[2]/div/div/div/div/div[3]/div/div/div/div/div/div[1]/div')
    element.screenshot("zhivaya.png")
    driver.close()
    return

parser()