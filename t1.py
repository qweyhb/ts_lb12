from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('https://www.figma.com/login?locale=en')
time.sleep(1)

username=browser.find_element(by=By.NAME, value='email')
username.send_keys('ekaterina_katkova0707@mail.ru')
time.sleep(1)

password=browser.find_element(by=By.NAME, value='password')
password.send_keys('QXCF637dg')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="auth-view-page"]/button[2]')
button.click()
time.sleep(10)

#Закрываем браузер
browser.close()
