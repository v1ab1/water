from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://aqua-mobil.ru/aktsii/aktsii_10.html")
    element = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div[2]')
    element.screenshot("aquamobil_2.png")
    driver.close()
    return