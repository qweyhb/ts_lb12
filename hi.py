from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

 # Получаем в переменную browser указатель на браузер
browser=webdriver.Chrome()
# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.figma.com/login?locale=en')
time.sleep(2)

# заполняем поле логин, привязываемся к элементу через его имя
username=browser.find_element(by=By.NAME, value='email')
username.send_keys('ekaterina_katkova0707@mail.ru')
time.sleep(1)

# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.NAME, value='password')
password.send_keys('Katkova200481')
time.sleep(10)

#Получаем указатель на кнопку "Вход"
button=browser.find_element(by=By.XPATH, value='//*[@id="auth-view-page"]/button[2]')
#Нажимаем на кнопку входа
button.click()
time.sleep(20)
#
#
button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div/div[2]/div[7]/div[3]')
#Нажимаем на кнопку входа
button.click()
time.sleep(5)
#
#
button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[3]/div/div/div[4]/div/button')
#Нажимаем на кнопку входа
button.click()
time.sleep(5)
#
#
teamname=browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[2]/div[1]/input')
teamname.send_keys('ekaterina2')
time.sleep(10)
#
#
button=browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div[2]/form/div[2]/button')
#Нажимаем на кнопку входа
button.click()
time.sleep(5)
#
#
email=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[2]/div[4]/div[1]/input[1]')
email.send_keys('potini3099@momoshe.com')
time.sleep(5)
#
#
button=browser.find_element(by=By.XPATH, value='//*[@id="react-page"]/div/div/div/div[1]/div[2]/div[4]/div[3]/button')
#Нажимаем на кнопку входа
button.click()
time.sleep(5)
#
#
button=browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/table/thead/tr/th[2]/div/button')
#Нажимаем на кнопку входа
button.click()
time.sleep(5)
#
actionChains = ActionChains(browser)
actionChains.context_click(button).perform()

# # Проверка результата
try:
    # Проверка что пользователь находится на странице авторизации
    assert 'Recently viewed' in browser.title
    errormessage=browser.find_element(by=By.ID, value='loginerrormessage')
    # Проверка сообщения об ошибке на странице
    assert 'Каткова Екатерина Егоровна' in errormessage.accessible_name
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
#
#Закрываем браузер
browser.close()
