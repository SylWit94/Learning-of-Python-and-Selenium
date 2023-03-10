import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.clothes_product_url = self.base_url + '3-clothes'
        self.art_product_url = self.base_url + '9-art'
        self.accessories_product_url = self.base_url + '6-accessories'
        self.login_url = self.base_url + 'login'
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

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
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title,
                         f'Expected {expected_title} differ from actual title {actual_title} on page: {url}')
