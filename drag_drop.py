from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver =  webdriver.Chrome()
url = "https://demoqa.com/droppable"
driver.get(url)
driver.maximize_window()

source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")
time.sleep(3)

actions = ActionChains(driver)

# actions.drag_and_drop(source,target).perform()
actions.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(5)

driver.quit()


