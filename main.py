from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.python.org/downloads/")
driver.implicitly_wait(8)
my_element = driver.find_element(By.CLASS_NAME,"donate-button")
my_element.click()