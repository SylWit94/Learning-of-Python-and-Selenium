import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.art_product_url = self.base_url + '9-art'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.login_url = self.base_url + 'login'
        driver = webdriver.Chrome(service=Service(executable_path=r'C:\TestFiles\New_driver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    @classmethod
    def tearDownClass(self):
        self.ef_driver.quit()

    def test_base_page_title(self):
        expected_title = 'Lost Hat'
        self.assert_title(self.base_url, expected_title)

    def test_product_clothes_page_title(self):
        expected_title = 'Clothes'
        self.assert_title(self.clothes_product_url, expected_title)

    def test_product_art_page_title(self):
        expected_title = 'Art'
        self.assert_title(self.art_product_url, expected_title)

    def test_product_accessories_page_title(self):
        expected_title = 'Accessories'
        self.assert_title(self.accessories_product_url, expected_title)

    def test_login_page(self):
        expected_title = 'Login'
        self.assert_title(self.login_url, expected_title)

    def get_page_title(self, url):
        self.ef_driver.get(url)
        return self.ef_driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')

    def test_of_product_searcher(self):
        expected_number_of_elements = 0
        driver = self.ef_driver
        driver.get(self.base_url)
        searcher_xpath = '//*[@id="search_widget"]//*[@type="text"]'
        searcher_element = driver.find_element(By.XPATH, searcher_xpath)
        searcher_element.send_keys('mug')
        magnifier_xpath = '//*[@id="search_widget"]/form/button/i'
        magnifier_element = driver.find_element(By.XPATH, magnifier_xpath)
        magnifier_element.click()

        list_of_products_xpath = '//*[@id="js-product-list"]/div/article'
        list_of_products_elements = driver.find_elements(By.XPATH, list_of_products_xpath)

        print(len(list_of_products_elements))

        self.assertGreater(len(list_of_products_elements), expected_number_of_elements,
                           f'The number of product element greater than {expected_number_of_elements}')