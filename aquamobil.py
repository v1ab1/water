from selenium import webdriver
from bs4 import BeautifulSoup
def parser():
    driver = webdriver.Firefox()
    driver.get("https://aqua-mobil.ru/voda-9-19-litrov/voda-artezianskaya-artenza-19-l-oborotnaya-tara.html")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    found = soup.find(class_='js-inprice')
    driver.close()
    return(found.text.strip())
