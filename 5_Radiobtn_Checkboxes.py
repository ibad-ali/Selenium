from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/"

driver.get(url)

#for checkboxes
a=driver.find_element_by_name('permission').is_selected()
b=driver.find_element_by_name('discardinfo').is_selected()
print(a)
print(b)

time.sleep(5)
#for radio buttons
status = driver.find_elements_by_name('sample')
for i in status:
    print(i.is_selected())


driver.close()