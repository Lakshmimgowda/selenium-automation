from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://demoqa.com/menu"
driver.get(url)
driver.maximize_window()

actions = ActionChains(driver)

element1 = driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
actions.move_to_element(element1).perform()
time.sleep(3)


element2 = driver.find_element(By.XPATH,"//a[normalize-space()='Sub Item']")
actions.move_to_element(element1).move_to_element(element2).perform()
time.sleep(2)

element3 = driver.find_element(By.XPATH,"//a[contains(text(),'SUB SUB')]3")
actions.move_to_element(element1).move_to_element(element2).move_to_element(element3).perform()
time.sleep(2)






