from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Launch Chrome browser
browser = webdriver.Chrome("chromedriver.exe")
# Open pypi.org
browser.get('https://pypi.org/project/selenium/')

# Maximize Browser Window
browser.maximize_window()

# Set wait time of 30 secs
browser.implicitly_wait(30)

# Type "Selenium" in search bar
browser.find_element(By.ID, 'search').send_keys("Selenium")
# Click Enter
browser.find_element(By.ID, 'search').send_keys(Keys.RETURN)
