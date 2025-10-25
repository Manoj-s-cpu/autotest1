import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir primera URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print("Pestaña 1: OrangeHRM abierta")
time.sleep(3)

# Abrir nueva pestaña y navegar a segunda URL
driver.switch_to.new_window('tab')
driver.get("https://practicetestautomation.com/practice-test-login/")
print("Pestaña 2: Practice Test Login abierta")
time.sleep(3)

# Abrir tercera pestaña
driver.switch_to.new_window('tab')
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
print("Pestaña 3: TutorialsPoint abierta")
time.sleep(3)

# Abrir cuarta pestaña
driver.switch_to.new_window('tab')
driver.get("https://demo.automationtesting.in/WebTable.html")
print("Pestaña 4: Automation Testing abierta")
time.sleep(3)

# Contar y mostrar todas las pestañas abiertas
total_tabs = len(driver.window_handles)
print(f"Total de pestañas abiertas: {total_tabs}")

# Mostrar los identificadores de ventana
for i, handle in enumerate(driver.window_handles):
    print(f"Pestaña {i + 1} handle: {handle}")

# Cambiar a la primera pestaña (OrangeHRM)
driver.switch_to.window(driver.window_handles[0])
print("Volviendo a la primera pestaña...")
time.sleep(2)

# Ejemplo: hacer clic en “Forgot your password?” en la primera pestaña
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
print("Clic realizado en 'Forgot your password?'")

time.sleep(3)
driver.quit()
