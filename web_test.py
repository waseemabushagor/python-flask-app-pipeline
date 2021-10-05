from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get("http://127.0.0.1:5000/edit")

time.sleep(3)

task = driver.find_element_by_xpath("/html/body/div/form/div/input")
task.send_keys('Test')
add = driver.find_element_by_xpath("/html/body/div/form/button")
add.click()

time.sleep(3)

update = driver.find_element_by_xpath("/html/body/div/div/a[1]")
update.click()

time.sleep(3)

delete = driver.find_element_by_xpath("/html/body/div/div/a[2]")
delete.click()

time.sleep(3)
driver.close()
driver.quit()

list_task = webdriver.Chrome('chromedriver_win32/chromedriver')
list_task.get("http://127.0.0.1:5000/")

time.sleep(3)

driver.close()
driver.quit()