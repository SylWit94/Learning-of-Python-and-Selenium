import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from helpers import functional_helper as fh


class LostHatLoginPageTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_login_text_header(self):
        expected_text = 'Log in to your account'
        header_xpath = '//header[@class="page-header"]'
        driver = self.driver
        driver.get(self.login_url)
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_correct_login(self):
        # expected_text is a user name and user surname used during registration
        expected_text = 'Sylwia Witkowska'
        user_email = 'sylwiaw57@wp.pl'
        user_pass = '12345678'
        user_name_xpath = '//*[@id="_desktop_user_info"]//*[@class="hidden-sm-down"]'
        driver = self.driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, user_name_xpath, expected_text)

    def test_incorrect_login(self):
        expected_text = 'Authentication failed.'
        user_email = 's@w.com'
        user_pass = '12345678'
        alert_xpath = '//*[@id="content"]//*[@class="alert alert-danger"]'
        driver = self.driver

        driver.get(self.login_url)
        fh.user_login(driver, user_email, user_pass)
        self.assert_element_text(driver, alert_xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver: webdriver instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text that we expect to be found
        :return: None
        """
        element = driver.find_element(By.XPATH, xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text,
                         f'Expected title differ from actual title for url: {driver.current_url}')

    def test_sanity_search_on_main_page(self):
        search_phrase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-Shirt'
        search_input_xpath = '//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        self.driver.get(self.base_url)
        search_input_element = self.driver.find_element(By.XPATH, search_input_xpath)
        search_input_element.send_keys(search_phrase)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.driver.find_elements(By.XPATH, result_element_xpath)
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1
        self.assertEqual(1, found_elements_number,
                         f"We expect 1 and actual number of found items is {found_elements_number}")

    def test_sanity_search_for_on_main_page(self):
        search_phrase = 'mug'
        expected_element_name = 'Customizable Mug'
        search_input_xpath = '//*[@id="search_widget"]//*[@name="s"]'
        result_element_xpath = '//*[@class="product-miniature js-product-miniature"]'
        self.driver.get(self.base_url)
        search_input_element = self.driver.find_element(By.XPATH, search_input_xpath)
        search_input_element.send_keys(search_phrase)
        search_input_element.send_keys(Keys.ENTER)
        result_elements = self.driver.find_elements(By.XPATH, result_element_xpath)
        found_elements_number = 0
        for element in result_elements:
            if expected_element_name in element.text:
                found_elements_number = found_elements_number + 1
        self.assertEqual(1, found_elements_number,
                         f'We expect 1 and actual number of found items is {found_elements_number}')
