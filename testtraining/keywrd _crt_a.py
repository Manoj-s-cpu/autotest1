from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Inicializar WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Localizar el campo de entrada de nombre de usuario
input_field = driver.find_element(By.ID, "user-name")

# Escribir texto inicial
input_field.send_keys("Hola Selenium, ¿cómo estás? ¿Qué estás haciendo ahora? Que tengas un buen día")
time.sleep(1)

# Crear instancia de ActionChains
actions = ActionChains(driver)

# Seleccionar todo el texto con Ctrl + A
actions.click(input_field).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
print("Texto seleccionado correctamente")
time.sleep(1)

# Limpiar el campo e introducir texto nuevo
input_field.clear()
input_field.send_keys("Guna Vision")
print("Nuevo texto ingresado correctamente")
time.sleep(2)

# Cerrar navegador
driver.quit()
