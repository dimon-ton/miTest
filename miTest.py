
import time
from selenium import webdriver

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


driver = webdriver.Chrome()

url = r'https://mi-test.obec.go.th/student/login.php'

driver.get(url)

time.sleep(5)

driver.close()

