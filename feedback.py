from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', [236895,236896,236897,236898,236899,236903,236904,236905])
def test_answer(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    textBox = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    textBox.send_keys(str(math.log(int(time.time()))))

    submitButton = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    submitButton.click()
    time.sleep(1)
    assert browser.find_element_by_css_selector("pre.smart-hints__hint").text == "Correct!", "The answer is not correct"
