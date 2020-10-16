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

# TO DO
# CREATE A FOR LOOP THAT LOOPS THROUGH ALL OF THE MAJOR CITIES



try: 
    driver.get('https://www.doordash.com/en-US')
    time.sleep(5)
    print('on the Doordash Home Page!')
except: 
    print('Could not find Doordash Page')
    driver.close()

try: 
    address_link = driver.find_element_by_class_name('sc-bkCOcH')
    address_button = driver.find_element_by_class_name('sc-ekQYnd')
    print('Found input and button')
except: 
    print('Could not find Doordash Input Form')

try: 
    address_link.send_keys('90403')
    time.sleep(0.5)
    address_button.click()
    time.sleep(5)
    print('Going to Doordash Restaurant page')
except: 
    print('Could not imput correct data')
    driver.close()

try:
    restaurant_link = driver.find_element_by_class_name('sc-bkCOcH')
    restaurant_link.send_keys('Mcdonalds')
    time.sleep(3)
except:
    print("Restaurant Link and Button Not Found on doordash")

try:
    # Finds the popup hover once there is data inserted into the input and clicks that hover
    restaurant_link_inner = driver.find_element_by_class_name('sc-bHwgHz')
    restaurant_link_inner.click()
    time.sleep(3)
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




