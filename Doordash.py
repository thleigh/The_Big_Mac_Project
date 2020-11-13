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
# , chrome_options=options

def doordash(data):
    driver = webdriver.Chrome(chrome_location, chrome_options=options)
    driver.get('https://www.doordash.com/en-US')
    time.sleep(5)

    try:
        address_link = driver.find_element_by_class_name('sc-bZJeJD')
        address_link.send_keys(data)
        time.sleep(3)
    except: 
        print('Could not input correct data')

    try:
        address_button = driver.find_element_by_xpath('.//*[@id="root"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/button')
        address_button.click()
        time.sleep(5)
        # print('Going to Doordash Restaurant page')
    except:
        print('Could not find button')

    try:
        restaurant_link = driver.find_element_by_class_name('sc-bZJeJD')
        restaurant_link.send_keys('Mcdonalds')
        time.sleep(3)
    except:
        print("Restaurant Link and Button Not Found on doordash")

    try:
        restaurant_link_inner = driver.find_element_by_class_name('sc-itybZL')
        restaurant_link_inner.click()
        time.sleep(5)
        # print('on the Mcdonalds page!')
    except:
        print('Could not find dropdown button')

    mcdonalds_prices = []
    try:
        prices = driver.find_elements_by_class_name('eEdxFA')
        for big_mac in prices:
            price = big_mac.text
            big_mac_price_parsed=price.split('\n')
            mcdonalds_prices.append(big_mac_price_parsed)
        big_mac_price = mcdonalds_prices[0]    
        for big_mac_prices in big_mac_price:
            results = {
                "location": data,
                "price": big_mac_prices[1:]
            } 
            # print( f'The Big Mac price in {data} is:', big_mac_prices)
            print(results)
        driver.close()
    except:
        print(f'Could not find the Big Mac Price for {data}')
    driver.quit()

def newDriver():
    driver = webdriver.Chrome(chrome_location, chrome_options=options)
    driver.get('https://www.doordash.com/en-US')