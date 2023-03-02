from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Launch driver instance
driver = webdriver.Chrome()

#Get the page
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Digital downloads").click()
time.sleep(2) 

#find total number of links in a page
links = driver.find_elements(By.TAG_NAME,'a') 
# Or can also be located using XPATh
links = driver.find_elements(By.XPATH,"//a")
print(len(links))

#Print all link names
for link in links:
    print(link.text)