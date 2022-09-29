import logging
import logging.handlers
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import traceback

from selenium.webdriver.common.keys import Keys

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()

logging.basicConfig(filename=f'Test{now}Protocol.log', filemode='w', format='%(name)s -%('
                                                                               'levelname)s -%('
                                                                               'message)s')
logging.warning(f'{today}_{current_time}_Programm gestartet')

from selenium.webdriver.remote.webelement import WebElement

# Auto anklicken und Bild anklicken

driver = webdriver.Chrome('/Users/janbenno/Desktop/IntelaJ/leasingNew/leasingNew/tests/chromedriver')
driver.get("https://www.frosty-morse.81-169-186-58.plesk.page/")
logging.warning(f'{today}_{current_time}_website aufgerufen')

try:
    assert "https://www.frosty-morse.81-169-186-58.plesk.page/" in driver.current_url
except AssertionError:
    logging.warning(f'{today}_{current_time}_fehlgeschlagen 1. assert')
    sys.exit()
logging.warning(f'{today}_{current_time}_assert erfolgreich')
driver.find_element(By.XPATH, "//a[@class='wp-block-button__link']").click()
logging.warning(f'{today}_{current_time}_button geklickt')
try:
    assert "https://www.frosty-morse.81-169-186-58.plesk.page/index.php/produkte/" in driver.current_url
except AssertionError:
    logging.warning(f'{today}_{current_time}_fehlgeschlagen')
    sys.exit()
# WebElement element = driver.find_element("//h1[@class='has-text-align-center has-nv-site-bg-color has-text-color']")
logging.warning(f'{today}_{current_time}_ProdukteSeite Aufgerufen')
try:
    assert "https://www.frosty-morse.81-169-186-58.plesk.page/index.php/produkte/" in driver.current_url
except AssertionError:
    logging.warning((f'{today}_{current_time}_fehlgeschlagen: Assertion false'))
    sys.exit()

driver.find_element(By.XPATH,
                    '(//div[@class="wc-block-components-product-image wc-block-grid__product-image"]/a)[1]').click()
logging.warning(f'{today}_{current_time}_1. auto angeklickt')
