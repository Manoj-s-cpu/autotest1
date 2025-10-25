from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)

actions = ActionChains(driver)

button = driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul/li[1]/a')
actions.click(button).perform()
print("Click realizado correctamente")
time.sleep(1)



driver.close()
