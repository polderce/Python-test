# импорт модулей time и selenium

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализация веб-драйвера с полным путем к исполняемому драйверу
driver = webdriver.Safari('/usr/bin/safaridriver')

# сон
time.sleep(2)

# открытие драйвером сайта
driver.get("https://www.saucedemo.com/")
time.sleep(1)


# поиск элементов формы по описанию в html коде
login = driver.find_element(By.NAME, "user-name")
password = driver.find_element(By.NAME, "password")

# отправка данных в найденные формы
login.send_keys("standard_user")
password.send_keys("secret_sauce")

time.sleep(1)


# поиск кнопки логина по xpath
driver.find_element('xpath', '//*[@id="login-button"]').click()
# метод click выполняет нажатие по кнопке формы

time.sleep(3)

driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

time.sleep(1)

driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()

time.sleep(1)

driver.find_element('xpath', '//*[@id="checkout"]').click()

time.sleep(1)

first_name = driver.find_element(By.NAME, "firstName")
last_name = driver.find_element(By.NAME, "lastName")
postal_code = driver.find_element(By.NAME, "postalCode")

first_name.send_keys("Михаил")
last_name.send_keys("Новиков")
postal_code.send_keys("132170")

time.sleep(1)

driver.find_element('xpath', '//*[@id="continue"]').click()

time.sleep(5)

driver.find_element('xpath', '//*[@id="finish"]').click()

time.sleep(10)
# окончание работы драйвера
driver.quit()