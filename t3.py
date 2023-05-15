from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome()
browser.get('https://www.figma.com/login?locale=en')
time.sleep(2)

username=browser.find_element(by=By.NAME, value='email')
username.send_keys('ekaterina_katkova0707@mail.ru')
time.sleep(1)

password=browser.find_element(by=By.NAME, value='password')
password.send_keys('QWEgfjs73d')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="auth-view-page"]/button[2]')
button.click()
time.sleep(20)

button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div/div[2]/div[7]/div[3]')
button.click()
time.sleep(5)

button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[3]/div/div/div[4]/div/button')
button.click()
time.sleep(5)

teamname=browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div[1]/input')
teamname.send_keys('ekaterina3')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[2]/button')
button.click()
time.sleep(5)

email=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[2]/div[4]/div[1]/input[1]')
email.send_keys('potini3099@momoshe.com')
time.sleep(1)

button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[2]/div[4]/div[3]/button')
button.click()
time.sleep(5)

button=browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[2]/div/button')
button.click()
time.sleep(5)

try:
    assert 'Figma' in browser.title
    assert "ekaterina3" in browser.page_source
    assert "Starter team" in browser.page_source
    print('Тест прошел удачно')
except Exception as err:
    print('Тест прошел неудачно')

#Закрываем браузер
browser.close()
