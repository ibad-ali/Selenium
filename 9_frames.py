from selenium.webdriver import Chrome
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "link"
driver.get(url)