from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Setup Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Step 2: Navigate to OrangeHRM demo login
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
time.sleep(2)

# Step 3: Click element using your XPath
xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
element = driver.find_element(By.XPATH, xpath)
element.click()
print("Element clicked!")
time.sleep(2)

# Step 4: Browser navigation examples

# Go back
driver.back()
print("Went back")
time.sleep(2)

# Go forward
driver.forward()
print("Went forward")
time.sleep(2)

# Refresh page
driver.refresh()
print("Page refreshed")
time.sleep(2)

# Step 5: Close browser
driver.quit()
