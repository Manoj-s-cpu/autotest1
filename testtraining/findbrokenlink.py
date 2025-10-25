import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(url)
time.sleep(2)

# Encontrar todos los enlaces
links = driver.find_elements(By.TAG_NAME, "a")
total_links = len(links)
print(f"Total links: {total_links}")
time.sleep(2)

# Verificar cada enlace
for link in links:
    href = link.get_attribute('href')
    if href:
        try:
            response = requests.get(href, timeout=3)
            if response.status_code >= 400:
                print(f"broken link: {href} (status code: {response.status_code})")
            
        except requests.exceptions.RequestException as e:
            print(f" Error accrossing {href}: {e}")

time.sleep(2)
driver.quit()
