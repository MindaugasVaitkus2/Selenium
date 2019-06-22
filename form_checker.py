
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'
link_list = [link1, link2]
i = 1
mistakes = 0
for each_list in link_list:
    browser.get(each_list)
    try:
        Name = browser.find_element_by_css_selector("[placeholder = 'Введите имя']")
        Name.send_keys("Ivan")
    except NoSuchElementException:
        print('\033[96mОБНАРУЖЕН БАГ:\033[0m', 'Элемент Name не найден')
        mistakes += 1
        
    try:
        Surname = browser.find_element_by_css_selector("[placeholder = 'Введите фамилию']")
        Surname.send_keys("Petrov")
    except NoSuchElementException:
        print('\033[96mОБНАРУЖЕН БАГ:\033[0m', 'Элемент Surname не найден')
        mistakes += 1
        
    try:
        Email = browser.find_element_by_css_selector("[placeholder = 'Введите Email']")
        Email.send_keys("Smolensk@gmail.com")
    except NoSuchElementException:
        print('\033[96mОБНАРУЖЕН БАГ:\033[0m', 'Элемент Email не найден')
        mistakes += 1

    try:
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    except NoSuchElementException:
        print('\033[96mОБНАРУЖЕН БАГ:\033[0m', 'Элемент Button не найден')
        mistakes += 1
    if mistakes == 0:
        time.sleep(2)
        try:
            welcome_text_elt = browser.find_element_by_tag_name('h1')
            Welcome_text = welcome_text_elt.text
        except NoSuchElementException:
            print('\033[96mОБНАРУЖЕН БАГ:\033[0m', 'Элемент welcome_text_elt не найден')

        try:
            assert 'Поздравляем! Вы успешно зарегестрировались!' == Welcome_text
            print ('Проверка пройдена')
        except AssertionError:
            print ('\033[96mОБНАРУЖЕН БАГ:\033[0m', 'Некорректное сообщение после регистрации.')
        print ('Форма регистрации №', i, ' проверена.')
        print ('Перехожу к проверке формы №', i+1)
    else:
        print ('Тестирование этой формы прервано, исправьте баги в форме.')
    mistakes = 0
    time.sleep(3)
print ('\nТестирование закончено')        
