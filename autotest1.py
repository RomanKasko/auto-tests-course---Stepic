from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    fName = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    fName.send_keys("Romeo")
    lName = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    lName.send_keys("Julietovich")
    email = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    email.send_keys("romeo@gmail.com")
    phone = browser.find_element_by_css_selector("div.second_block input.form-control.first")
    phone.send_keys("228")
    address = browser.find_element_by_css_selector("div.second_block input.form-control.second")
    address.send_keys("not Earth")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
