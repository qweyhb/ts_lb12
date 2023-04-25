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
time.sleep(20)

button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[3]/div[6]/div[2]/a[1]')
button.click()
time.sleep(5)

#Закрываем браузер
browser.close()