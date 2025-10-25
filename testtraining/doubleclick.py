from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(2)

actions = ActionChains(driver)

double_click_button = driver.find_element(By.XPATH, '//*[@id="authentication"]/button')

actions.double_click(double_click_button).perform()
print("Paso 1: Double-click exitoso")

time.sleep(1)
alert = driver.switch_to.alert
print(f"Alert detectado: {alert.text}")
alert.accept()
print("Alert aceptado")

time.sleep(2)
driver.quit()
