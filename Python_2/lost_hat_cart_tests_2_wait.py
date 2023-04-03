import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.events import EventFiringWebDriver

from helpers.screenshot_listener import ScreenshotListener


class LostHatShoppingCartTests(unittest.TestCase):

    def setUp(self):
        self.subpage_accessories_url = 'https://autodemo.testoneo.com/en/6-accessories'
        driver = webdriver.Chrome(service=Service(executable_path=r'C:\TestFiles\New_driver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    def tearDown(self):
        self.ef_driver.quit()

    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '×\n\ue876Product successfully added to your shopping cart'
        item_xpath = '//*[@id="js-product-list"]//*[@data-id-product = "7"]'
        driver = self.ef_driver
        driver.get(self.subpage_accessories_url)
        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()

        button_add_to_cart_xpath = '//*[@id="add-to-cart-or-refresh"]//*[@class="btn btn-primary add-to-cart"]'
        button_element = driver.find_element(By.XPATH, button_add_to_cart_xpath)
        button_element.click()

        modal_element_xpath = '//*[@id="blockcart-modal"]//*[@class="modal-header"]'
        modal_element = WebDriverWait(driver.wrapped_driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, modal_element_xpath)), f'Element not found')

        self.assertEqual(expected_confirmation_modal_text, modal_element.text)
