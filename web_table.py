from xml.dom.minidom import Element

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
time.sleep(2)
driver.maximize_window()
elements = driver.find_element(By.XPATH, "//h5[text()='Elements']")
scroll = driver.execute_script("arguments[0].scrollIntoView();",elements)
time.sleep(2)
elements.click()
time.sleep(2)
elements_click=driver.find_element(By.CSS_SELECTOR, ".element-list.accordion-collapse.collapse.show").click()
time.sleep(3)
print("clicked")
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Web Tables").click()
time.sleep(3)

Full_Table= driver.find_elements(By.XPATH, "//table//tr")  #print full_table
for row in Full_Table:
    print(row.text + "  ")

rows = driver.find_elements(By.XPATH, "//table//tr") # to print len of rows
print(len(rows))
# for row in rows:
#     print(row.text)

cols = driver.find_elements(By.XPATH, "//table//th") #to print len of cols
print(len(cols))
for col in cols:# print the value of cols
    print(col.text)
#
row1 = driver.find_elements(By.XPATH, "//table//tr[1]") #print specific row
for row in row1:
    if "Cierra" in row.text:
        print(row.text)

table_row = driver.find_elements(By.XPATH, "//table//tr")
for row in table_row:
    table_col=row.find_elements(By.XPATH, ".//th | .//td") # to ittirate within the row
    for col in table_col:
        print(col.text, end='  ')
    print()

rows = driver.find_elements(By.XPATH, "//table//tr")   # to delete the specific row
for row in rows:
    if "Cierra Vega" in row.text:
        delete_btn = row.find_element(By.XPATH, ".//span[starts-with(@id,'delete-record')]")
        delete_btn.click()
        print("Deleted successfully")
        break


