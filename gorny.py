from seleniumwire import webdriver
from bs4 import BeautifulSoup
import json
from seleniumwire.utils import decode
def parser():
    driver = webdriver.Firefox()
    driver.scopes = [
        '.*74mv.ru/index*'
    ]
    driver.get('https://www.74mv.ru/katalog/gornyj-oazis/%D0%B2%D0%BE%D0%B4%D0%B0-%D0%BF%D0%B8%D1%82%D1%8C%D0%B5%D0%B2%D0%B0%D1%8F-%D0%B3%D0%BE%D1%80%D0%BD%D1%8B%D0%B9-%D0%BE%D0%B0%D0%B7%D0%B8%D1%81-%D0%BD%D0%B5%D0%B3%D0%B0%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-19,0%D0%BB-detail')
    response = driver.last_request.response
    jsoned = json.loads(decode(response.body, response.headers.get('Content-Encoding', 'identity')))
    out = str(jsoned["unitPrice"])
    driver.close()
    return(out.split()[0][0:3])
