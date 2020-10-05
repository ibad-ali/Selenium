from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

webdriver = "E:\\chromedriver.exe"

driver = Chrome(webdriver)

url = "https://onecore.net"

driver.get(url)

print(driver.title) #return title of the website
print(driver.current_url) #return current url of website
driver.find_element_by_xpath('//*[@id="menu-item-1086"]/a').click() # go to url after clicking
time.sleep(5) #wait for the 5 second

driver.close() # close current browser
#driver.quit() # close all browser
