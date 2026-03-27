from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver =webdriver.Chrome()
driver.get("https://demoqa.com/")
time.sleep(2)
form = driver.find_element(By.XPATH, "//h5[text()='Forms']")
viewport = driver.execute_script("arguments[0].scrollIntoView();", form)
time.sleep(3)
form.click()
time.sleep(3)
practice_form = driver.find_element(By.LINK_TEXT,"Practice Form")
time.sleep(3)
practice_form.click()
time.sleep(3)

first_name = driver.find_element(By.ID,"firstName").send_keys("jai")
time.sleep(2)
last_name= driver.find_element(By.ID,"lastName").send_keys("Anjaneya")
time.sleep(2)
email = driver.find_element(By.ID,"userEmail").send_keys("jaiAnjaneya@gmail.com")
time.sleep(3)
radio_button = driver.find_element(By.ID,"gender-radio-1").click()
time.sleep(3)
Mobile_number = driver.find_element(By.ID,"userNumber").send_keys("7676918212")
time.sleep(3)
Date_of_birth = driver.find_element(By.ID,"dateOfBirthInput").click() #handle calendar
time.sleep(2)
Month = Select(driver.find_element(By.CLASS_NAME,"react-datepicker__month-select"))
Month.select_by_visible_text("February")
time.sleep(3)
year = Select(driver.find_element(By.CLASS_NAME,"react-datepicker__year-select"))
year.select_by_visible_text("2025")
time.sleep(3)
day =driver.find_element(By.XPATH,"//div[text()='19']")
day.click()
time.sleep(3)
subject = driver.find_element(By.ID,"subjectsInput")
subject.send_keys("Comp")
time.sleep(4)
subject.send_keys(Keys.ENTER)
time.sleep(3)

# sport = driver.find_element(By.ID,"subjects-label") #to check particular check box
# sport.click()
check_box = driver.find_elements(By.XPATH, "//label[@for='hobbies-checkbox']") #check all the check boxes
for i in check_box:
    if not i.is_selected():
        i.click()
    time.sleep(5)
    print("selected checkboxes are:",i.text)
labels = driver.find_elements(By.XPATH, "//label[contains(@for,'hobbies-checkbox')]") # check all the check box
for i in labels:
    i.click()
    time.sleep(3)
    print("selected checkbox:", i.text)# print the selected checkbox

file_upload = driver.find_element(By.ID,"uploadPicture") #upload pic
time.sleep(3)
file_upload.send_keys("F:\\ganesha\\IMG_3858.JPG")
time.sleep(3)

Address = driver.find_element(By.ID,"currentAddress").send_keys("949kuvempu rd pappreddy palya")
time.sleep(3)

state =driver.find_element(By.ID, "state")
state.click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()
time.sleep(3)
print("selected state is:", state.text)

city = driver.find_element(By.ID, "city") # to select the city
city.click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()
print("selected city is:", city.text)

# Submit_button = driver.find_element(By.ID,"submit")
# Submit_button.click()
# time.sleep(3)
# popup = driver.find_element(By.ID, "example-modal-sizes-title-lg")
# time.sleep(3)
# if popup.is_displayed():
#
#     print("popup is displayed")
driver.find_element(By.ID, "submit").click()
print("Submit clicked")
time.sleep(5)
popup = driver.find_element(By.XPATH, "//div[text()='Thanks for submitting the form']")

print("Popup is displayed ✅")
print("Popup text:", popup.text)




