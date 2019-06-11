from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#así abro navegador chrome
#navegador = webdriver.Chrome()
#así abro nagegador ie
navegadorIE = webdriver.Ie()
time.sleep(2)
navegadorIE.get("https://www.google.com/")
time.sleep(2)
navegadorIE.maximize_window()
time.sleep(2)
buscador = navegadorIE.find_element_by_name('q')
#buscador.clear()   #es opcional
buscador.send_keys('buenas noches a todos')
buscador.send_keys(Keys.RETURN)
time.sleep(2)
navegadorIE.close()