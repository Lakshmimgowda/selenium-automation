from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome()
# driver.get("https://jqueryui.com/datepicker/")
# driver.maximize_window()

# iframe = driver.find_element(By.TAG_NAME, "iframe")
# driver.switch_to.frame(iframe)
# time.sleep(2)


# target_month = "April"
# target_year = "2026"
# target_day = "4"
#
# calendar = driver.find_element(By.ID, "datepicker").click()     #target date
# while True:
#     month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#
#     if month == target_month and year == target_year:
#         break
#     else:
#         driver.find_element(By.XPATH, "//a[@title='Next']").click()
# time.sleep(2)

# calendar = driver.find_element(By.ID, "datepicker").click() #todays date
#
# today_date = driver.find_element(By.CLASS_NAME, "ui-datepicker-today")
# print(today_date.text)
# time.sleep(2)

# prev_month = "February"
# prev_date = "19"
# prev_year = "2025"
#
# calendar = driver.find_element(By.ID, "datepicker").click()
# while  True:
#     month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#
#     if month == prev_month and year == prev_year:
#         print("you found the date")
#         break
#     else:
#         driver.find_element(By.XPATH, "//a[@title='Prev']").click()
#         time.sleep(2)

# Month = "December"  # prev and next
# Date = "30"
# Year = "2028"
#
# calendar = driver.find_element(By.ID, "datepicker").click()
# while True:
#     month=driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
#     year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
#
#     if year == Year and month == Month:
#         print("you found the date")
#         break
#     elif int(year) < int(Year):
#         driver.find_element(By.XPATH, "//a[@title='Next']").click()
#     elif int(year) > int(Year):
#         driver.find_element(By.XPATH, "//a[@title='Prev']").click()
#
#     else:
#         months = ["January", "February", "March", "April", "May", "June",
#                   "July", "August", "September", "October", "November", "December"]
#
#         if months.index(month) < months.index(Month):
#             driver.find_element(By.XPATH, "//a[@title='Next']").click()
#         else:
#             driver.find_element(By.XPATH, "//a[@title='Prev']").click()
#     time.sleep(3)

# DROP DOWN CALENDAR

driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")
driver.maximize_window()
calendar = driver.find_element(By.ID, "datePickerMonthYearInput")
target_month = "January"
target_date = "30"
target_year = "2020"

calendar.click()
while True:
    month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month.select_by_value(target_month)
    date = Select(driver.find_element(By.ID, "datePickerMonthYearInput"))



