from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# #
# name = driver.find_element(By.XPATH,"//input[@id='name']")
# name.send_keys("lakshmi")
# time.sleep(2)
# #
# email = driver.find_element(By.XPATH,"//input[@id='email']")
# email.send_keys("lakshmikl@gmail.com")
# time.sleep(2)
# #
# # phone = driver.find_element(By.XPATH,"//input[@id='phone']")
# # phone.send_keys("7676918212")
# # time.sleep(2)

# address = driver.find_element(By.ID,"textarea")
# address.send_keys("#949 kuvempu rd nagarbhavi")
# time.sleep(2)

# radio = driver.find_element(By.XPATH,"//input[@id='female']")
# radio.click()
# time.sleep(2)

#to select single checkbox
# Single_checkbox = driver.find_element(By.XPATH,"//input[@id='monday']")
# Single_checkbox.click()
# time.sleep(2)
# #
# # #to select all the checkbox
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# for i in checkboxes:
#     if not i.is_selected():
#         i.click()
#     time.sleep(5)

#to select the dropdown
# dropdown = Select(driver.find_element(By.ID,"country"))
# dropdown.select_by_value("india")
# time.sleep(5)
# print(dropdown.first_selected_option.text)
# time.sleep(2)

# To scroll
# colors = driver.find_element(By.XPATH,"//label[contains(text(),'Color')]")
#driver.execute_script("arguments[0].scrollIntoView();",colors)
#time.sleep(2)
# print(colors.is_displayed())

# colour = Select(driver.find_element(By.ID,"colors"))
# colour.select_by_value("green")
# print(colour.first_selected_option.text)

#date picker
# calendar1 = driver.find_element(By.XPATH,"//input[@id='datepicker']")
# calendar1.click()
# target_month = "February"
# target_date = 19
# target_year = 2020
#
# while True:
#     month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
#     year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text
#
#     if month == target_month and int(year)  == target_year:
#         break
#     elif int(year) >target_year:
#         driver.find_element(By.XPATH, "//a[@title='Prev']").click()
#         time.sleep(2)
#     elif int(year) <target_year:
#         driver.find_element(By.XPATH, "//a[@title='Next']").click()
#         time.sleep(2)
#     else:
#         months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
#         if months.index(month) < months.index(target_month):
#             driver.find_element(By.XPATH, "//a[@title='Next']").click()
#         else:
#             driver.find_element(By.XPATH, "//a[@title='Prev']").click()
# driver.find_element(By.XPATH, f"//a[text()='{target_date}']").click()
#
# time.sleep(3)

#dropdown calendar
# calendar2 = driver.find_element(By.XPATH, "//input[@id='txtDate']")
# calendar2.click()
# time.sleep(3)
# target_m = "Jan"
# target_y = "2025"
# target_d = 20
#
# month = Select(driver.find_element(By.CLASS_NAME,"ui-datepicker-month"))
# month.select_by_visible_text(target_m)
# time.sleep(3)
#
# year = Select(driver.find_element(By.CLASS_NAME,"ui-datepicker-year"))
# year.select_by_visible_text(target_y)
# time.sleep(3)
#
# date = driver.find_element(By.XPATH, f"//a[text()='{target_d}']").click()
# time.sleep(3)

# start and end range calendar
start_date = driver.find_element(By.ID, "start-date")
start_date.send_keys("01-20-2025")
time.sleep(3)

end_date = driver.find_element(By.ID, "end-date")
end_date.send_keys("01-21-2025")
time.sleep(3)

submit = driver.find_element(By.XPATH, "//button[@class='submit-btn']")
submit.click()

result = driver.find_element(By.XPATH, "//div[@class='result']")
print(result.text)