from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://voda174.ru/")
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[10]')
    element.screenshot("crystal.png")
    driver.close()
    return