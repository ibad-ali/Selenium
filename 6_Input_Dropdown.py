from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "https://gpacalculator.net/college-gpa-calculator/"
driver.get(url)

drp = Select(driver.find_element_by_xpath('//*[@id="calcframebs"]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/span/select'))
print(len(drp.options))

opts = drp.options
for i in opts:
    print(i.text)


driver.close()