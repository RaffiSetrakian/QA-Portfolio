import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from Day14 import excelUtils

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://www.calculatestuff.com/financial/compound-interest-calculator?utm_source=chatgpt.com")
driver.maximize_window()

file = "/Users/raff__s/Desktop/Interest Calculator Data.xlsx"

rows = excelUtils.getRowCount(file,"Sheet1")

for row in range(2, rows+1):
    # Reading data from Excel
    principal = excelUtils.readData(file,"Sheet1",row,1)
    interestrate = excelUtils.readData(file,"Sheet1",row,2 )
    compounding = excelUtils.readData(file,"Sheet1",row,3)
    term = excelUtils.readData(file,"Sheet1",row,4)
    exp_fvalue = excelUtils.readData(file,"Sheet1",row,5)

    # Passing Data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").clear()
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principal)
    driver.find_element(By.XPATH, "//input[@id='interest_rate']").clear()
    driver.find_element(By.XPATH,"//input[@id='interest_rate']").send_keys(interestrate)
    comp = Select(driver.find_element(By.XPATH,"//select[@id='compound_frequency']"))
    comp.select_by_visible_text(compounding)
    driver.find_element(By.XPATH, "//input[@id='term']").clear()
    driver.find_element(By.XPATH,"//input[@id='term']").send_keys(term)
    driver.find_element(By.XPATH,"//input[@id='calculate-button']").click()

    act_fvalue = driver.find_element(By.XPATH,"//div[@class='row big bold']/div[@class='col-xs-4 col-lg-7']").text

    # Validation
    if  exp_fvalue == act_fvalue:
        print("test passed")
        excelUtils.writeData(file,"Sheet1",row,6,act_fvalue)
        excelUtils.writeData(file,"Sheet1",row,8, "Passed ")
        excelUtils.fillGreenColdr(file,"Sheet1",row,8)
    else:
        print("test failed")
        excelUtils.writeData(file, "Sheet1", row, 6, act_fvalue)
        excelUtils.writeData(file, "Sheet1", row, 8, "Failed")
        excelUtils.fillRedColor(file, "Sheet1", row, 8)

    time.sleep(2)

driver.quit()
