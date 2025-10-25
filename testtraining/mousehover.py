import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://practice.expandtesting.com/hovers"
driver.get(url)

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

hover_element1 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="core"]/div/div/div[1]/img')
))
driver.execute_script("arguments[0].scrollIntoView(true);", hover_element1)
actions.move_to_element(hover_element1).perform()
print("Paso 1: OK")
time.sleep(2)

hover_element2 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="core"]/div/div/div[2]/img')
))
driver.execute_script("arguments[0].scrollIntoView(true);", hover_element2)
actions.move_to_element(hover_element2).perform()
print("Paso 2: OK")
time.sleep(2)

hover_element3 = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="core"]/div/div/div[3]/img')
))
driver.execute_script("arguments[0].scrollIntoView(true);", hover_element3)
actions.move_to_element(hover_element3).perform()
print("Paso 3: OK")
time.sleep(2)


driver.quit()
