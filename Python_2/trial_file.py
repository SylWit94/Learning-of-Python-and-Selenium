import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from helpers import search_expression_helper as seh


class LostHatTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_number_of_mug_search_results(self):
        expected_text = 'There are 5 products.'
        search_expression = 'mug'
        search_element_xpath = '//*[@id="search_widget"]//*[@placeholder="Search our catalog"]'
        search_result_number_xpath = '//*[@id="js-product-list-top"]//*[@class="col-md-6 hidden-sm-down total-products"]/p'
        magnifier_element_xpath = '//*[@id="search_widget"]/form/button/i'
        driver = self.driver
        driver.get(self.base_url)
        seh.search_element(driver, search_expression)
        # search_element = driver.find_element(By.XPATH, search_element_xpath)
        # search_element.send_keys(search_expression)
        # time.sleep(2)
        # magnifier_element = driver.find_element(By.XPATH, magnifier_element_xpath)
        # magnifier_element.click()
        # time.sleep(2)
        self.assert_element_text(driver, search_result_number_xpath, expected_text)

    def test_number_of_tshirt_search_results(self):
        expected_text = 'There is 1 product.'
        search_expression = 't-shirt'
        search_element_xpath = '//*[@id="search_widget"]//*[@placeholder="Search our catalog"]'
        search_result_number_xpath = '//*[@id="js-product-list-top"]//*[@class="col-md-6 hidden-sm-down total-products"]/p'
        magnifier_element_xpath = '//*[@id="search_widget"]/form/button/i'
        driver = self.driver
        driver.get(self.base_url)
        seh.search_element(driver, search_expression)
        # search_element = driver.find_element(By.XPATH, search_element_xpath)
        # search_element.send_keys(search_expression)
        # time.sleep(2)
        # magnifier_element = driver.find_element(By.XPATH, magnifier_element_xpath)
        # magnifier_element.click()
        # time.sleep(2)
        self.assert_element_text(driver, search_result_number_xpath, expected_text)

    def test_number_of_accessories_products(self):
        expected_text = 'There are 11 products.'
        accessories_element_xpath = '//*[@id="category-6"]/a'
        driver = self.driver
        driver.get(self.base_url)
        accessories_element = driver.find_element(By.XPATH, accessories_element_xpath)
        accessories_element.click()
        search_result_number_xpath = '//*[@id="js-product-list-top"]//p'
        self.assert_element_text(driver, search_result_number_xpath, expected_text)

    def test_language(self):
        expected_text = 'English'
        language_xpath = '//*[@id="_desktop_language_selector"]//*[@class="expand-more"]'
        driver = self.driver
        driver.get(self.base_url)
        self.assert_element_text(driver, language_xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

        :param driver: webdriver instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text that we expect to be found
        :return: None
        """
        element = driver.find_element(By.XPATH, xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual for url: {driver.current_url}')


class LostHatFrontPageTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_product_image_minimum_size(self):
        expected_min_height = 200
        expected_min_width = 200
        image_xpath = '//*[@id="content"]/section/div/article[1]/div/a/img'
        driver = self.driver

        driver.get(self.base_url)
        image_element = driver.find_element(By.XPATH, image_xpath)
        actual_image_height = image_element.size['height']
        actual_image_width = image_element.size['width']

        self.assertLess(expected_min_height, actual_image_height,
                        f'Expected height found by xpath {image_xpath} on page {driver.current_url} is smaller than expected {expected_min_height}px')
        self.assertLess(expected_min_width, actual_image_width,
                        f'Expected width found by xpath {image_xpath} on page {driver.current_url} is smaller than expected {expected_min_width}px')

    def test_slider_contains_exact_number_of_slides(self):
        expected_slides_number = 3
        # xpath_slider = '//*[@id="carousel"]'
        xpath_slides = '//*[@id="carousel"]/ul/li'
        driver = self.driver

        driver.get(self.base_url)
        slides_elements = driver.find_elements(By.XPATH, xpath_slides)
        actual_slides_number = len(slides_elements)

        self.assertEqual(expected_slides_number, actual_slides_number,
                         f'Expected number of slides is differ from actual: {actual_slides_number} for url: {driver.current_url}')

    def test_slides_contains_required_text(self):
        expected_text_included_in_slide = 'sample'
        xpath_slides_titles = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        driver = self.driver

        driver.get(self.base_url)
        title_slides_elements = driver.find_elements(By.XPATH, xpath_slides_titles)

        for title_slides_element in title_slides_elements:
            title_slides_element_text = title_slides_element.get_attribute("textContent")
            title_slides_element_text_lower = title_slides_element_text.lower()
            print(title_slides_element_text_lower)
        self.assertIn(expected_text_included_in_slide, title_slides_element_text_lower,
                      f"Slides doesn't contain expected text for page: {self.base_url}")
