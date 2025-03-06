from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time # type: ignore
import random
# for Search engine
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# To find Search box
elem = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')
#To Type keys
elem.send_keys('flipcart')
# To Enter
elem.send_keys(Keys.ENTER)
time.sleep(2)
# To click link
elem = driver.find_element(By.XPATH, '//*[@id="r1-0"]/div[2]/div/div/a/div/p/span').click()
time.sleep(3)
# In Amazone
elem = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
elem.send_keys('Phone')
elem.send_keys(Keys.ENTER)
time.sleep(2)
# To scroll
driver.execute_script("window.scrollTo(0,1500)")
time.sleep(2)
#Random clicking
clickable_elements = driver.find_elements(By.XPATH, '//a | //button')
if clickable_elements:
    random_element = random.choice(clickable_elements)
    random_element.click()
    time.sleep(5)
else:
    print("No clickable elements found")
# Add to cart
elem = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
time.sleep(5)
driver.close()