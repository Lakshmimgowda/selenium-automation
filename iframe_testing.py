from traceback import print_tb

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/guru99home/")
driver.maximize_window()
time.sleep(5)

iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(len(iframes))              #to find length of the  iframes
for i in range (len(iframes)):
    print(i)     #print  index of iframe
    print(iframes[i].get_attribute("src"))  #print the iframe link/name
    print(iframes[i].get_attribute("name"))
    print(iframes[i].get_attribute("id"))

youtube = driver.find_element(By.XPATH, "//iframe[contains(@src,'youtube')]")
print("clicked:", youtube.get_attribute("src"))
driver.switch_to.frame(youtube)
time.sleep(5)




