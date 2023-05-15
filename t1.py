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
password.send_keys('QWEgfjs73d')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="auth-view-page"]/button[2]')
button.click()
time.sleep(10)

try:
    assert 'Figma' in browser.title
    assert "Ekaterina" in browser.page_source
    print('Тест прошел удачно')
except Exception as err:
    print('Тест прошел неудачно')

#Закрываем браузер
browser.close()
