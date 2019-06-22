from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/explicit_wait2.html')

wait_for_better_price = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '10000'))
button = driver.find_element(By.ID, 'book').click()
                                                                                  
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

find_x = driver.find_element_by_css_selector('span#input_value.nowrap')
x = find_x.text
y = calc(x)
find_answer = driver.find_element_by_id('answer')
find_answer.send_keys(y)
button_element = driver.find_element_by_css_selector("button#solve.btn.btn-primary")
button_element.click()

