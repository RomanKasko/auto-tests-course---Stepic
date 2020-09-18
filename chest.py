from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chest = browser.find_element_by_id("treasure")
    x = chest.get_attribute("valuex")

    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))

    notRobotCheck = browser.find_element_by_id("robotCheckbox")
    notRobotCheck.click()

    rButton = browser.find_element_by_id("robotsRule")
    rButton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()