# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.Amazon.ca")
driver.maximize_window()
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
electronics_link = driver.find_element("xpath","//*[@id='nav-xshop']/a[7]")
electronics_link.click()

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Electronics: Amazon.ca" in driver.title

# Selecting a course from the search results
Smartwatches_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/div[1]/ul[1]/li[11]/a")
# Course_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
Smartwatches_link.click()



# Waiting for the laptop details page to load
time.sleep(5)

# Adding the laptop to the cart
watch_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/div/div[2]/div[2]/ul/li[5]/span/div/a/div/div")
watch_link.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
wishlist_link= driver.find_element("xpath","/html/body/div[2]/div/div[6]/div[4]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[7]/div[1]/div[1]/span/span/a")
wishlist_link.click()
time.sleep(2)



# Closing the webdriver
driver.close()
