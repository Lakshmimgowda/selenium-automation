

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://docs.stripe.com/payments/accept-a-payment")
driver.maximize_window()
time.sleep(3)

# get all parent iframes
# parent_frames = driver.find_elements(By.TAG_NAME, "iframe")
# print("Total parent frames:", len(parent_frames))
#
# for i in range(len(parent_frames)):
#     driver.switch_to.default_content()  # go back to main page
#
#     parent_frames = driver.find_elements(By.TAG_NAME, "iframe")  # re-fetch
#     driver.switch_to.frame(parent_frames[i])  # switch to parent frame
#
#     print(f"\nParent Frame {i}:")
#
#     # find child iframes inside this parent
#     child_frames = driver.find_elements(By.TAG_NAME, "iframe")
#     print(f"Number of child frames inside Parent {i}: {len(child_frames)}")
#
# driver.quit()

parent_frames = driver.find_elements(By.TAG_NAME, "iframe")
print("the total iframes are:",len(parent_frames),)

for i in range(len(parent_frames)):
    driver.switch_to.default_content()


    parent_frames = driver.find_elements(By.TAG_NAME, "iframe")
    print(parent_frames[i].get_attribute("src"))
    driver.switch_to.frame(parent_frames[i])

    child_frames = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"number of child in parents frames are{i}-{len(child_frames)}")