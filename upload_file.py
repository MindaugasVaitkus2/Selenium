from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'send_keys.txt')

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/file_input.html')
find_name = driver.find_element_by_css_selector("[placeholder = 'Введите имя']")
find_name.send_keys('Dan')
find_surname = driver.find_element_by_css_selector("[placeholder = 'Введите фамилию']")
find_surname.send_keys("mats")
find_email =  driver.find_element_by_css_selector("[placeholder = 'Введите Email']")
find_email.send_keys("tratata@mail.ru")
find_choose_file = driver.find_element_by_css_selector("[accept = '.txt']")
find_choose_file.send_keys(file_path)
button = driver.find_element_by_css_selector('button.btn.btn-primary').click() 

