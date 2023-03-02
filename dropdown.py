import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

#Launch driver instance
driver = webdriver.Chrome()

#Get the page
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

#Get element
# drpcountry_elem = driver.find_element(By.XPATH,"//select[@id='input-country']")

# Pass elements in select class of selenium by finding drop elements
drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#select option from the drop down
# drpcountry.select_by_visible_text("Cuba")
# Or
drpcountry.select_by_value("10")
# # Or
drpcountry.select_by_index(11)

time.sleep(2)

#Capture all the options and print them
alloptions = drpcountry.options
print(len(alloptions))

for option in alloptions:
    print(option.text)


# Get options without Select class of selenium
allOpts = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print(len(allOpts))
