import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.devtools.v137.fed_cm import click_dialog_button
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

# filling the name/email/phone/address
driver.find_element(By.ID,"name").send_keys("John Smith")
driver.find_element(By.ID,"email").send_keys("example@gmail.com")
driver.find_element(By.ID,"phone").send_keys("0987654321")
driver.find_element(By.ID,"textarea").send_keys("5th ave.")

# Choosing gender
driver.find_element(By.ID,"male").click()

# Selecting a week day
weekdays = driver.find_elements(By.XPATH,"//label[contains(text(), 'day')]")

for days in weekdays :
    if days.text == "Sunday" or days.text == "Saturday":
        days.click()

# Selecting a country
country = driver.find_element(By.XPATH,"//select[@id='country']")
select1 = Select(country)
select1.select_by_visible_text("Canada")

# Selecting a color
colors = driver.find_element(By.XPATH, "//select[@id='colors']")
select2 = Select(colors)
select2.select_by_visible_text("Red")

# selecting an animal
animals = driver.find_element(By.XPATH, "//select[@id='animals']")
select3 = Select(animals)
select3.select_by_visible_text("Rabbit")

# ----------------------------------date picker 1----------------------------------
driver.find_element(By.ID,"datepicker").click()
month = "November"
year = "2026"
day = "12"

# month and year selection
while True:
    yearele = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
    monthele = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
    if monthele.text == month and yearele.text == year :
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

daysele = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")
for dayele in daysele:
    if dayele.text == day:
        dayele.click()

# ----------------------------------date picker 2----------------------------------
driver.find_element(By.NAME, "SelectedDate").click()
month2 = driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
selectMM = Select(month2)
selectMM.select_by_visible_text("Nov")

year2 = driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
selectYYYY = Select(year2)
selectYYYY.select_by_visible_text("2026")

days3 = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")
for day3 in days3 :
    if day3.text == "24" :
        day3.click()

# ----------------------------------date picker 3----------------------------------
driver.find_element(By.ID, "start-date").send_keys("12111999")
driver.find_element(By.ID, "end-date").send_keys("12112026")
driver.find_element(By.XPATH, "//button[@class='submit-btn']").click()

# printing the rows that have the Author name Mukesh
table = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody")
rowss = table.find_elements(By.TAG_NAME, "tr")

for row in rowss[1:]:
    cells = row.find_elements(By.TAG_NAME,"td")
    if cells[1].text == "Mukesh":
        for cell in cells :
            print(cell.text, end="  ")
        print(" ")

# Dynamic button START
driver.find_element(By.XPATH,"//button[contains(text(), 'ST')]").click()

# Alerts
driver.find_element(By.ID,"alertBtn").click()
time.sleep(2)
driver.switch_to.alert.accept()
driver.find_element(By.ID, "confirmBtn").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
driver.find_element(By.ID, "promptBtn").click()
driver.switch_to.alert.send_keys("Muhammad Ali")
time.sleep(2)
driver.switch_to.alert.accept()

# Dynamic button STOP
driver.find_element(By.XPATH,"//button[contains(text(), 'ST')]").click()

# Mouse Hover
action = ActionChains(driver)

pointme = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
mobiles = driver.find_element(By.XPATH, "//a[normalize-space()='Mobiles']")
laptops = driver.find_element(By.XPATH, "//a[normalize-space()='Laptops']")

action.move_to_element(pointme).perform()
time.sleep(2)
action.move_to_element(mobiles).perform()
time.sleep(2)
action.move_to_element(laptops).perform()

# double click
field1 = driver.find_element(By.ID, "field1")
field1.clear()
field1.send_keys("Mike Tyson")

dblclickbtn = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
action.double_click(dblclickbtn).perform()

# Drag and drop
sourceele = driver.find_element(By.ID, "draggable")
targetele = driver.find_element(By.ID,"droppable")

action.drag_and_drop(sourceele , targetele).perform()

# sliders
minimum = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
maximum = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[2]")
print("minimums current location : ", minimum.location) # {'x': 927, 'y': 2027}
print("maximums current location : ", maximum.location) # {'x': 1057, 'y': 2027}

action.drag_and_drop_by_offset(minimum, -600, 0).perform()
action.drag_and_drop_by_offset(maximum, 300, 0).perform()

print("minimums after moving location : ", minimum.location)
print("maximums after moving location : ", maximum.location)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value) # 3405.5

time.sleep (5)
#Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #0