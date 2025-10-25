from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)

actions = ActionChains(driver)

right_click = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
actions.context_click(right_click).perform()
time.sleep(4)
driver.quit