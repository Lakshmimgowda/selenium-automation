from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()

driver.find_element(By.NAME,"cusid").send_keys("123456789")
driver.find_element(By.NAME,"submit").click()
time.sleep(2)

alert = driver.switch_to.alert
time.sleep(2)
alert.accept()
print(alert.text)
time.sleep(2)

alert2 = driver.switch_to.alert
time.sleep(2)
print(alert2.text)
alert2.accept()
