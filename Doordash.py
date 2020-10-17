from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import datetime, re, requests, io, time, random, string
from chrome_driver import chrome_location

options = Options()
options.add_argument('--disable-extensions')
options.add_argument('--window-size=800,600')
options.add_argument('--proxy-byprass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.set_headless(True)

# locates the chrome_driver app in the local system
driver = webdriver.Chrome(chrome_location, chrome_options=options)
# , chrome_options=options

# Thought Process

# 1. Loop through major cities, one at a time
# 2. Start Selenium inputing that city
# 3. If no data is returned, restart and enter next city
# 4. If data is returned, save data, close selenium and go to next city.


def doordash(data):
    try: 
        driver.get('https://www.doordash.com/en-US')
        time.sleep(5)
        print('on the Doordash Home Page!')
    except: 
        print('Could not find Doordash Page')

    try: 
        address_link = driver.find_element_by_class_name('sc-bkCOcH')
        address_link.send_keys(data)
        time.sleep(3)
    except: 
        print('Could not imput correct data')

    try:
        address_button = driver.find_element_by_xpath('.//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/button')
        address_button.click()
        time.sleep(5)
        print('Going to Doordash Restaurant page')
    except:
        print('Could not find button')

    try:
        restaurant_link = driver.find_element_by_class_name('sc-bkCOcH')
        restaurant_link.send_keys('Mcdonalds')
        time.sleep(3)
    except:
        print("Restaurant Link and Button Not Found on doordash")

    try:
        restaurant_link_inner = driver.find_element_by_class_name('sc-bHwgHz')
        restaurant_link_inner.click()
        time.sleep(5)
        print('on the Mcdonalds page!')
    except:
        print('Could not find dropdown button')

    mcdonalds_prices = []
    try:
        prices = driver.find_elements_by_class_name('eEdxFA')
        for big_mac in prices:
            price = big_mac.text
            big_mac_price_parsed=price.split('\n')
            mcdonalds_prices.append(big_mac_price_parsed)
        big_mac_price = mcdonalds_prices[1]    
        print(big_mac_price)
    except:
        print('Could not find the Big Mac Price')