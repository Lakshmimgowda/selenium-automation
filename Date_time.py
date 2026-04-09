from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
time.sleep(2)

# today_date = datetime.now() # to select today date
# print(today_date.strftime("%d/%m/%Y")) # to select the date and print the date day and month

target = datetime(2019, 2, 28)

target_date = str(target.day)
target_month = target.strftime("%B")
target_year = str(target.year)

calendar = driver.find_element(By.ID,"datepicker").click()

while True:
    month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
    year= driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text

    if int(target_year)==int(year) and month==target_month:
        print("the value is found")
        break
    elif int(target_year) < int(year):
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()
        time.sleep(1)
    elif int(target_year) > int(year):
        driver.find_element(By.XPATH, "//a[@title='Next']").click()
        time.sleep(1)
    else:
        month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        current_month = datetime.strptime(month,"%B").month
        target_month = target.strftime("%B")
        if current_month == target_month:
            break
        elif current_month > int(target_month):
            driver.find_element(By.XPATH, "//a[@title='Prev']").click()
            time.sleep(1)
        elif current_month < int(target_month):
            driver.find_element(By.XPATH, "//a[@title='Next']").click()
            time.sleep(1)

date = driver.find_element(By.CLASS_NAME,"ui-state-default").click()
for i in date:
    if i.text == target_date:
        date.click()

