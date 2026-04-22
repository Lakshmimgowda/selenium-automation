from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
text = driver.find_element(By.TAG_NAME, "p")
if "congraulations" in text.text:
    print("congraulation")
else:
    print("not congraulation")