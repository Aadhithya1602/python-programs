from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time # type: ignore
import pandas as pd
# for Search engine
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# To find Search box
elem = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')
#To Type keys
elem.send_keys('Flipkart')
# To Enter
elem.send_keys(Keys.ENTER)
time.sleep(2)
# To click link
elem = driver.find_element(By.XPATH, '//*[@id="r1-0"]/div[2]/div/div/a/div/p/span').click()
time.sleep(3)
# In flipcart
elem = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
time.sleep(3)
elem.send_keys('phones')
elem.send_keys(Keys.ENTER)
# scraping
product_names = []
elem1 = driver.find_elements(By.CLASS_NAME, 'KzDlHZ')
for product_name, in zip(elem1):
    print("Phone Name:", product_name.text)
    product_names.append(product_name.text)
    time.sleep(1)
product_prices = []
elem2 = driver.find_elements(By.CLASS_NAME, 'Nx9bqj._4b5DiR')
for product_price, in zip(elem2):
    print("Phone price:", product_price.text)
    product_prices.append(product_price.text)
    time.sleep(1)
    product_offers = []
elem3 = driver.find_elements(By.CLASS_NAME, 'yRaY8j.ZYYwLA')
for product_offer, in zip(elem3):
    print("Phone offerprice:", product_offer.text)
    product_offers.append(product_offer.text)
    time.sleep(1)
# Close the browser
driver.quit()
#Print the lengths of the lists
print(f"Number of product names: {len(product_names)}")
print(f"Number of product prices: {len(product_prices)}")
print(f"Number of product offers: {len(product_offers)}")
# Check lengths of the lists
len_names = len(product_names)
len_prices = len(product_prices)
len_offers = len(product_offers)
# If lengths are not equal, pad the shorter lists
max_length = max(len_names, len_prices, len_offers)
# Pad shorter lists with None
product_names.extend([None] * (max_length - len_names))
product_prices.extend([None] * (max_length - len_prices))
product_offers.extend([None] * (max_length - len_offers))
# file name
file_name = 'bluedata.xlsx'
#saving execl
df = pd.DataFrame({
    'Phone Name': product_names,
    'Phone price': product_prices,
    'Phone offerprice': product_offers
})
df.to_excel(file_name, index=False)
print('DataFrame is written to Excel File successfully.')