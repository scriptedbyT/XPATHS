from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Get absolute path to sample HTML
file_path = f"file://{os.getcwd()}/sample_pages/sample1.html"

driver = webdriver.Chrome()
driver.get(file_path)

# XPath examples
username_input = driver.find_element(By.XPATH, "//input[@id='username']")
username_input.send_keys("Taneshka")

password_input = driver.find_element(By.XPATH, "//input[@type='password']")
password_input.send_keys("123456")

login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'login')]")
login_button.click()

mango_item = driver.find_element(By.XPATH, "//li[text()='Mango']")
print("Found item:", mango_item.text)

time.sleep(2)
driver.quit()