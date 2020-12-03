from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "link"
driver.get(url)

#driver.switch_to_alert().dismiss()
#driver.switch_to_alert().accept()

time.sleep(3)

driver.close()