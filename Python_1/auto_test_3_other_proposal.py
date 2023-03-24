import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from selenium.webdriver.chrome.service import Service
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_button_dalej_is_disabled_when_login_input_is_empty(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_form_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_form_input_element.clear()

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_disabled = login_next_button_element.get_property('disabled')
        self.assertEqual(True, login_next_button_disabled,
                         f'Expected state of "dalej" button: True , differ from actual: {login_next_button_disabled} , for page url: {url}')