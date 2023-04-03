import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener


class LostHatFrontPageTests(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://autodemo.testoneo.com/en/'
        driver = webdriver.Chrome(service=Service(executable_path=r'C:\TestFiles\New_driver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    def tearDown(self):
        self.ef_driver.quit()

    def test_slider(self):
        slider_xpath = '//*[@id="carousel"]'
        driver = self.ef_driver

        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, slider_xpath)

    def test_slider_minimum_size(self):
        expected_min_height = 300
        expected_min_width = 600
        slider_xpath = '//*[@id="carousel"]'
        driver = self.ef_driver

        driver.get(self.base_url)
        slider_element = driver.find_element(By.XPATH, slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']

        with self.subTest('Element height'):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Expected height found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_height}px')

        with self.subTest('Element width'):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Expected width found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_width}px')

    def test_slider_contain_exact_number_of_slides(self):
        expected_number_of_slides = 3
        slides_xpath = '//*[@id="carousel"]/ul/li'
        driver = self.ef_driver

        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, slides_xpath)
        actual_number_of_slides = len(slider_elements)

        self.assertEqual(expected_number_of_slides, actual_number_of_slides,
                         f'Slides number differ for page {self.base_url}')

    def test_slides_required_title_text(self):
        expected_text_included_in_slide = 'sample'
        slides_titles_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
        driver = self.ef_driver

        driver.get(self.base_url)
        title_elements = driver.find_elements(By.XPATH, slides_titles_xpath)

        for title_element in title_elements:
            title_element_text = title_element.get_attribute("textContent")
            title_element_text_lower = title_element_text.lower()
            with self.subTest(title_element_text_lower):
                self.assertIn(expected_text_included_in_slide, title_element_text_lower,
                              f"Slides does not contain expected text for page {self.base_url}")

    def test_main_website_contains_exact_number_of_products(self):
        expected_product_number = 8
        xpath_products = '//*[@id="content"]/section/div/article'
        driver = self.ef_driver

        driver.get(self.base_url)
        products = driver.find_elements(By.XPATH, xpath_products)
        actual_products_number = len(products)
        self.assertEqual(expected_product_number, actual_products_number,
                         f'Expected number of product at main website is differ from actual for {self.base_url}')

    def test_main_website_contains_exact_number_of_product_second_solution(self):
        expected_number = 8
        product_xpath = '//*[@class="product-miniature js-product-miniature"]'
        driver = self.ef_driver

        driver.get(self.base_url)
        product_elements = driver.find_elements(By.XPATH, product_xpath)
        actual_number_of_products = len(product_elements)
        self.assertEqual(expected_number, actual_number_of_products, f'Products number differ for page {self.base_url}')

    # def test_loop_usage(self):
    #     expected_text_included_in_string = 'star'
    #     list_of_items = ['stargate', 'starship', 'cat', 'stardust', 'startreck', 'dog']
    #
    #     for item in list_of_items:
    #         print('item')
    #
    #     for item in list_of_items:
    #         item_text_lower = item.lower()
    #         with self.subTest(f'Failed item is {item}'):
    #             self.assertIn(expected_text_included_in_string, item_text_lower,
    #                   f'Slides does not contain expected text for page {self.base_url}')

    def test_sanity_all_products_have_price_in_pln(self):
        expected_product_currency = 'PLN'
        product_prices_xpath = '//*[@id="content"]//*[@class="price"]'
        self.ef_driver.get(self.base_url)
        result_elements = self.ef_driver.find_elements(By.XPATH, product_prices_xpath)
        for result_element in result_elements:
            result_element_text = result_element.get_attribute("textContent")
            with self.subTest(result_element_text):
                self.assertIn(expected_product_currency, result_element_text,
                              f'Expected text not found in product description for page {self.base_url}')
