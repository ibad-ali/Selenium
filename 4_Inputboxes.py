from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "https://volunteersignup.org/register"

driver.get(url)

txtboxes = driver.find_elements_by_class_name('form-control')
print(len(txtboxes)) #gives the number of txt boxes on the form
time.sleep(3)

#fill the text boxes one by one

driver.find_element_by_name('firstname').send_keys("Ibad")
driver.find_element_by_name('lastname').send_keys("Ali")
driver.find_element_by_name('organisation').send_keys("Student")
driver.find_element_by_name('username').send_keys("ibadalink@gmail.com")
driver.find_element_by_name('username_verify').send_keys("ibadalink@gmail.com")
driver.find_element_by_name('password').send_keys("Nokia100")
driver.find_element_by_name('password_verify').send_keys("Nokia100")

time.sleep(3)

driver.close()