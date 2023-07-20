
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.edge.service import Service

path = r'C:\Users\saich\Documents\miTest\msedgedriver.exe'

service = Service(path)

driver = webdriver.Edge(service=service)

url = r'https://mi-test.obec.go.th/student/login.php'

driver.get(url)


# login to mi-test
user_elem = driver.find_element(By.NAME, 'user_em')

password_elem = driver.find_element(By.NAME, 'password_em')

user_elem.send_keys("1139600699752")

password_elem.send_keys("1234")


submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()

print("click submit: ", submit)







time.sleep(5)

driver.close()

