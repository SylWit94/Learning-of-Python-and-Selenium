import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener


class LostHatProductPageTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'
        driver = webdriver.Chrome(service=Service(executable_path=r'C:\TestFiles\New_driver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    def tearDown(self):
        self.ef_driver.quit()

    def test_check_product_name(self):
        expected_text = 'HUMMINGBIRD PRINTED T-SHIRT'
        name_xpath = '//*[@class="col-md-6"]//*[@itemprop="name"]'
        driver = self.ef_driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, name_xpath, expected_text)

    def test_check_product_price(self):
        expected_text = 'PLN23.52'
        price_xpath = '//*[@class="current-price"]//*[@itemprop="price"]'
        driver = self.ef_driver

        driver.get(self.sample_product_url)
        self.assert_element_text(driver, price_xpath, expected_text)

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