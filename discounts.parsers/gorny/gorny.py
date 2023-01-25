from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve


def parser():
    driver = webdriver.Firefox()
    driver.get("https://www.74mv.ru/aktsii")
    img_element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/p[2]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "gorny_1.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/p[2]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "gorny_2.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/p[2]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "gorny_3.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[2]/div/div[2]/div/div[4]/p[2]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "gorny_4.jpg")
    driver.quit()