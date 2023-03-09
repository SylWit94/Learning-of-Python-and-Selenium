import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from helpers import operational_helper as oh


class LostHatShoppingCartTests(unittest.TestCase):

    def setUp(self):
        self.subpage_art_url = 'https://autodemo.testoneo.com/en/9-art'
        self.driver = webdriver.Chrome(service=Service(executable_path=r'C:\TestFiles\chromedriver.exe'))

    def tearDown(self):
        self.driver.quit()

    def test_adding_item_to_shopping_cart(self):
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'
        # expected_confirmation_modal_text = 'Product successfully added to your shopping cart'
        item_xpath = '//*[@id="js-product-list"]//*[@data-id-product="12"]'
        driver = self.driver
        driver.get(self.subpage_art_url)
        item_element = driver.find_element(By.XPATH, item_xpath)
        item_element.click()

        button_add_to_cart_xpath = '//*[@id="add-to-cart-or-refresh"]//*[@class="btn btn-primary add-to-cart"]'
        element_button_add_to_cart = driver.find_element(By.XPATH, button_add_to_cart_xpath)
        element_button_add_to_cart.click()

        confirmation_modal_element_xpath = '//*[@id="myModalLabel"]'
        # time.sleep(3)
        confirmation_modal_elements = oh.wait_for_elements(driver, confirmation_modal_element_xpath, 5)
        confirmation_modal_element = driver.find_element(By.XPATH, confirmation_modal_element_xpath)
        confirmation_modal_element_text = confirmation_modal_element.text

        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element_text,
                         f'The expected confirmation text differ from actual for {driver.current_url}')

        # self.assertIn(expected_confirmation_modal_text, element_confirmation_modal_label_text,
        #               f'The expected confirmation text differ from actual for {driver.current_url}')
