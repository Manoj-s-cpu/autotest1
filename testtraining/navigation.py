from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
time.sleep(2)

xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
element = driver.find_element(By.XPATH, xpath)
element.click()
print("Element clicked!")
time.sleep(2)

driver.back()
print("Went back")
time.sleep(2)

driver.forward()
print("Went forward")
time.sleep(2)

driver.refresh()
print("Page refreshed")
time.sleep(2)

driver.quit()
