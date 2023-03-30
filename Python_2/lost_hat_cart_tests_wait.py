# In this file I have implemented the functionality of doing screenshots in the case of occurring the except in WebDriver
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver

from helpers import operational_helper as oh
from helpers.screenshot_listener import ScreenshotListener


class LostHatShoppingCartTests(unittest.TestCase):

    def setUp(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        driver = webdriver.Chrome(service=Service(executable_path=r'C:\TestFiles\New_driver\chromedriver.exe'))
        self.ef_driver = EventFiringWebDriver(driver, ScreenshotListener())

    def tearDown(self):
        self.ef_driver.quit()

    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        # expected_confirmation_modal_text = 'Product successfully added to your shopping cart'
        item_xpath = '//*[@id="js-product-list"]//*[@data-id-product="12"]'
        driver = self.ef_driver
        driver.get(self.subpage_art_url)
        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()

        button_add_to_cart_xpath = '//*[@id="add-to-cart-or-refresh"]//*[@class="btn btn-primary add-to-cart"]'
        element_button_add_to_cart = driver.find_element(By.XPATH, button_add_to_cart_xpath)
        element_button_add_to_cart.click()

        confirmation_modal_element_xpath = '//*[@id="myModalLabel"]'
        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_element_xpath)
        # confirmation_modal_element = WebDriverWait(driver, 10).until(
        #     ec.visibility_of_element_located((By.XPATH, confirmation_modal_element_xpath)),
        #     f'Element for xpath: {confirmation_modal_element_xpath} and url: {driver.current_url} not found')

        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)
