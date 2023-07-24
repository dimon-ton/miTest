
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from readCSV import readFromCSV


from selenium.webdriver.edge.service import Service

path = r'C:\Users\saich\Documents\miTest\msedgedriver.exe'

service = Service(path)




# get ID from csv file
ID_list = readFromCSV("ID.CSV")



for ID in ID_list:

	
	driver = webdriver.Edge(service=service)

	url = r'https://mi-test.obec.go.th/student/login.php'
	
	print("This is ID:", ID)

	driver.get(url)


	# login to mi-test
	user_elem = driver.find_element(By.NAME, 'user_em')

	password_elem = driver.find_element(By.NAME, 'password_em')

	
	ID = ID.strip()
	user_elem.send_keys(ID)

	password_elem.send_keys("1234")


	submit = driver.find_element(By.XPATH, "//button[@type='submit']")

	submit.click()
	

	driver.get('https://mi-test.obec.go.th/student/index.php?module=form_std&id=0')

	myRadios = driver.find_elements(By.XPATH, '//input[@type="radio"]')


	# count the number of radio elements in test.

	n = [0,1]


	amount = len(myRadios)/2
	for i in range(int(amount)):
		random_n = random.choices(n, weights=(40, 60), k=1)
		if random_n == [1]:
			driver.find_element(By.ID, "r[{}]".format(i+1)).click()

	# driver.find_element(By.ID, "r[1]").click()
	# driver.find_element(By.ID, "r[3]").click()

	# click submit button to send data
	submit1 = driver.find_element(By.XPATH, '//center/button[@type="submit"]').click()


	time.sleep(10)

	driver.close()


