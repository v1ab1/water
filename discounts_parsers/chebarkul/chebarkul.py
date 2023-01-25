from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve


async def parser():
    driver = webdriver.Firefox()
    driver.get("https://chebistok.ru/")
    img_element = driver.find_element(By.XPATH, '/html/body/div[3]/section[2]/div/div/div[2]/div[3]/div[2]/img[2]')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "./discounts_parsers/chebarkul/chebarkul_1.jpg")
    img_element = driver.find_element(By.XPATH, '/html/body/div[3]/section[2]/div/div/div[2]/div[3]/div[1]/img[2]')
    img_url = img_element.get_attribute('src')
    urlretrieve(img_url, "./discounts_parsers/chebarkul/chebarkul_2.jpg")
    driver.quit()