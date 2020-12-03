from selenium.webdriver import Chrome
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "https://www.duplichecker.com/"
driver.get(url)

#get all the links of web page
links = driver.find_elements_by_tag_name('a')
for i in links:
    print(i.text)

#click on any particular link

driver.find_element_by_class_name('navbar-brand').click()
time.sleep(3)


driver.close()