from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/alert_accept.html')
try:
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    driver.switch_to.alert.accept()
    time.sleep(1)

    x_element = driver.find_element(By.ID, 'input_value')
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.TAG_NAME, 'Button').click()
finally:
    time.sleep(5)
    driver.quit()
