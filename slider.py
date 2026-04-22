from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "https://demoqa.com/slider"
driver.get(url)

actions = ActionChains(driver)
slider = driver.find_element(By.ID, "slider")
# time.sleep(2)
# actions.drag_and_drop_by_offset(slider,60,80).perform()

value = slider.get_attribute("value")
#
# assert int(value) >50
# print(value)

# (actions.click(slider).move_to_element_with_offset(slider,60,0)
#                       .release().perform())
# time.sleep(2)
# print(slider.get_attribute("value"))
#
# target = 80
# while True:
#     actions = ActionChains(driver)
#     value = slider.get_attribute("value")
#     if int(value) == target:
#         break
#     elif int(value) < target:
#         actions.click_and_hold(slider).move_by_offset(5,0).release().perform()
#     elif int(value) > target:
#         actions.click_and_hold(slider).move_by_offset(-5,0).release().perform()
#      print(value)
#
# driver.close()

