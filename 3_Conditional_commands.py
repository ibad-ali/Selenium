from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)
driver.get("https://www.turnitin.com/")
time.sleep(3)
driver.find_element_by_xpath('/html/body/header/div[2]/section[2]/div/div[2]/div/a[2]').click()

element = driver.find_element_by_name('email')

print(element.is_displayed())
print(element.is_enabled())
print(element.is_selected())

password = driver.find_element_by_name('user_password')
print(password.is_displayed())
print(password.is_enabled())
print(password.is_selected())

time.sleep(3)

element.send_keys("ibadalink@gmail.com")
password.send_keys("Nokia100")

time.sleep(3)

driver.find_element_by_xpath('//*[@id="ibox_form_body"]/div[3]/input').click()

time.sleep(3)

driver.close()