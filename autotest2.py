from selenium import webdriver
import time
import unittest

def commonLink(link):
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

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text

class TestUI(unittest.TestCase):
    def test_link1(self):
        link = commonLink("http://suninjuly.github.io/registration1.html")
        self.assertEqual(link,"Congratulations! You have successfully registered!",
                         f"Submit message should be 'Congratulations! You have successfully registered!', but we got {link}")

    def test_link2(self): #This function must return error
        link = commonLink("http://suninjuly.github.io/registration2.html")
        self.assertEqual(link,"Congratulations! You have successfully registered!",
                         f"Submit message should be 'Congratulations! You have successfully registered!', but we got {link}")


if __name__ == "__main__":
    unittest.main()
