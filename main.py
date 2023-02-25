from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Users/votho/OneDrive/Documents/Development/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(1)

language = driver.find_element(by=By.ID, value="langSelect-EN")
language.click()
time.sleep(1)

cookie = driver.find_element(by=By.ID, value="bigCookie")
start_time = time.time()
increment = 5
while True:
    if time.time() > increment + start_time:
        try:
            upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#upgrades .enabled")
            if upgrades:
                for item in upgrades[::-1]:
                    item.click()
            else:
                print("No upgrades available")

            products = driver.find_elements(by=By.CSS_SELECTOR, value=".product.enabled")
            if products:
                for item in products[::-1]:
                    item.click()
            else:
                print("Not enough cookies")
        except:
            print("Error occurred")
        start_time = time.time()
        increment += 5
    try:
        cookie.click()
    except NoSuchElementException:
        print("Error occurred")
        break


driver.quit()
