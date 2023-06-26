from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import random
from random import randint
import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select


# options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# user-agent
options.add_argument(u)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
s = Service(executable_path="D:\python projects\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver = undetected_chromedriver.Chrome()
    driver.set_window_size(2560, 1440)
    driver.get("https://boutique.hublot.com/eur_en/nftclaim/form/luckydraw/")
    time.sleep(5)

    email_input = driver.find_element_by_name("email")
    email_input.clear()
    email_input.send_keys(my)
    time.sleep(5)


    name_input = driver.find_element_by_name("firstname")
    name_input.clear()
    name_input.send_keys(b)
    time.sleep(3)

    last_input = driver.find_element_by_name("lastname")
    last_input.clear()
    last_input.send_keys(n)
    time.sleep(3)

    phone_input = driver.find_element_by_name("phone")
    phone_input.clear()
    phone_input.send_keys("93", randint(1000000, 9999999))

    reg_choice = driver.find_element_by_xpath('//*[@id="phone_prefix"]').click()
    region_choice = driver.find_element_by_xpath('//*[@id="phone_prefix"]')
    select = Select(region_choice)
    select.select_by_value('UA')
    accept_button = driver.find_element_by_xpath('//*[@id="optin_tc"]').click()

    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()