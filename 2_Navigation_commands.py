from selenium.webdriver import Chrome
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

driver.get('https://onecore.net/')
print(driver.title)
time.sleep(2)
driver.get('https://www.duplichecker.com/')
print(driver.title)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
driver.quit()