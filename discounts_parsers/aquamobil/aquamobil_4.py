from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve


async def parser():
    driver = webdriver.Firefox()
    driver.get("https://aqua-mobil.ru/aktsii/aktsii_16.html")
    img_element = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div[2]/div/div[5]/img')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "./discounts_parsers/aquamobil/aquamobil_4.jpg")
    driver.quit()