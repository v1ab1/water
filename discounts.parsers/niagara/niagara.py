from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time

def parser():
    driver = webdriver.Firefox()
    driver.get("https://niagara74.ru/stock/#aktsii-na-dostavke")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_0.jpg")

    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[1]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_1.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_2.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[3]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_3.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[4]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_4.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[5]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_5.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[6]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_6.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[7]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_7.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div[8]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_del_8.jpg")

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/ul/li[2]/a').click()
    time.sleep(2)

    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_1.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_2.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_3.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_4.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[5]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_5.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[6]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_6.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[7]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_7.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[8]/a/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "niagara_store_8.jpg")

    driver.close()
    return

parser()