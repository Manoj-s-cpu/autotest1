import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------
# Inicializar driver
# -------------------------
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://demo.automationtesting.in/Alerts.html"
driver.get(url)
time.sleep(2)

# -------------------------
# Crear WebDriverWait
# -------------------------
wait = WebDriverWait(driver, 10)

# -------------------------
# Paso 1: Simple Alert
# -------------------------
simple_alert = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="OKTab"]/button'))
)
simple_alert.click()
time.sleep(1)

alertas = driver.switch_to.alert
print("Paso 1: OK alert")
alertas.accept()
time.sleep(2)

# -------------------------
# Paso 2: Confirmation Alert
# -------------------------
# Click en la pestaña "Alert with OK & Cancel"
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()

# Esperar a que el botón sea clickeable
confirm_alert = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="CancelTab"]/button'))
)
confirm_alert.click()
time.sleep(1)

# Aceptar confirm alert
confirm_alerts = driver.switch_to.alert
print("Paso 2: Confirmation alert - Accept")
confirm_alerts.accept()
time.sleep(2)

# Volver a hacer clic para probar dismiss
confirm_alert.click()
confirm_alerts = driver.switch_to.alert
print("Paso 2: Confirmation alert - Dismiss")
confirm_alerts.dismiss()
time.sleep(2)

driver.quit()

#  mouse hover--------------------------------------------------------------------------------------