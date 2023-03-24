import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LostHatSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.art_url = self.base_url + '9-art'
        self.clothes_url = self.base_url + '3-clothes'
        self.accessories_url = self.base_url + '6-accessories'
        self.login_url = self.base_url + 'login'
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    def setUp(self):
        pass

    def test_title_main_page(self):
        expected_title = 'Lost Hat'
        driver = self.driver

        driver.get(self.base_url)
        self.assert_title(driver, expected_title)

    def test_title_art_page(self):
        expected_title = 'Art'
        driver = self.driver

        driver.get(self.art_url)
        self.assert_title(driver, expected_title)

    def test_title_clothes_page(self):
        expected_title = 'Clothes'
        driver = self.driver

        driver.get(self.clothes_url)
        self.assert_title(driver, expected_title)

    def test_title_accessories_page(self):
        expected_title = 'Accessories'
        driver = self.driver

        driver.get(self.accessories_url)
        self.assert_title(driver, expected_title)

    def test_title_login_page(self):
        expected_title = 'Login'
        driver = self.driver

        driver.get(self.login_url)
        self.assert_title(driver, expected_title)

    def assert_title(self, driver, expected_title):
        title = driver.title
        self.assertEqual(expected_title, title, f'Expected title differ from actual for url: {driver.current_url}')

    def test_of_product_searcher(self):
        expected_number_of_elements = 0
        driver = self.driver
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

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
