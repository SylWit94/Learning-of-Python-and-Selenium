import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LostHatTests(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.art_url = self.base_url + '9-art'
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        xpath = '//header[@class="page-header"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, xpath, expected_text)

    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'Sylwia Witkowska'
        user_email = 'sylwiaw57@wp.pl'
        user_pass = '12345678'
        user_name_xpath = '//*[@id="_desktop_user_info"]//*[@class="hidden-sm-down"]'
        driver = self.driver
        driver.get(self.login_url)

        self.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_email = 's@w.com'
        user_pass = '12345678'
        alert_xpath = '//*[@id="content"]//*[@class="alert alert-danger"]'
        driver = self.driver
        driver.get(self.login_url)

        self.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)

    def test_check_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        driver = self.driver
        driver.get(self.sample_product_url)

        self.assert_element_text(driver, name_xpath, expected_text)

    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        driver = self.driver
        driver.get(self.sample_product_url)

        self.assert_element_text(driver, price_xpath, expected_text)

    def user_login(self, driver, user_email, user_pass):
        # finding login input box and sending value
        login_input_element = driver.find_element(By.XPATH, '//*[@type="email"]')
        login_input_element.send_keys(user_email)

        # finding password input box and sending value
        login_input_element = driver.find_element(By.XPATH, '//*[@type="password"]')
        login_input_element.send_keys(user_pass)

        # finding button 'sign in'
        button_next_element = driver.find_element(By.XPATH, '//*[@id="submit-login"]')
        button_next_element.click()

    def assert_element_text(self, driver, xpath, expected_text):
        element = driver.find_element(By.XPATH, xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected title differ from actual title for url: {driver.current_url}')


def add_numbers(number_one, number_two):
    result = number_one + number_two
    return result


result = add_numbers(2, 9)
print(result)


def substract_numbers(number_one, number_two):
    result = number_one - number_two
    return result


result = substract_numbers(10, 1)
print(result)


def multiplicate_numbers(number_one, number_two):
    result = number_one * number_two
    return result

result = multiplicate_numbers(3, 7)
print(result)
