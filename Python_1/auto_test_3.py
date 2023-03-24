import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# class MainTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         from selenium.webdriver.chrome.service import Service
#         self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
#
#     def test_demo_login(self):
#         driver = self.driver
#         url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
#         driver.get(url)
#         title = driver.title
#         print(f'Actual title: {title}')
#         self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
#                          f'Expected title differ from actual for page url: {url}')
#
#     def test_demo_accounts(self):
#         driver = self.driver
#         url = 'https://demobank.jaktestowac.pl/konta.html'
#         driver.get(url)
#         title = driver.title
#         print(f'Actual title: {title}')
#         self.assertEqual('Demobank - Bankowość Internetowa - Konta', title,
#                          f'Expected title differ from actual for page url: {url}')
#
#     def test_demo_pulpit(self):
#         driver = self.driver
#         url = 'https://demobank.jaktestowac.pl/pulpit.html'
#         driver.get(url)
#         title = driver.title
#         print(f'Actual title: {title}')
#         self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title,
#                          f'Expected title differ from actual for page url: {url}')
#
#     def test_demo_transfer(self):
#         driver = self.driver
#         url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
#         driver.get(url)
#         title = driver.title
#         print(f'Actual title: {title}')
#         self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title,
#                          f'Expected title differ from actual for page url: {url}')
#
#     @classmethod
#     def tearDownClass(self):
#         self.driver.quit()


class LoginPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from selenium.webdriver.chrome.service import Service
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # def test_login_page_title(self):
    #     driver = self.driver
    #     url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
    #     driver.get(url)
    #     # title = driver.title
    #     # print(f'Actual title: {title}')
    #
    #     login_form_header_element = driver.find_element(By.XPATH, '//*[@id="header_1"]')
    #     login_form_header_element_text = login_form_header_element.text
    #     print(f'Login form header text: {login_form_header_element_text}')
    #
    #     self.assertEqual('Wersja demonstracyjna serwisu demobank', login_form_header_element_text,
    #                      f'Expected form header text differ from actual for url: {url}')

    def test_next_button_disability(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element_text = login_input_element.text
        login_input_element.clear()
        print(f'Login input initial text: {login_input_element_text}')

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element_disabled_property = login_next_button_element.get_property('disabled')
        print(f'If boolean True?: {login_next_button_element_disabled_property == True}')

        login_input_element.send_keys('syl_wit')
        login_input_element_value = login_input_element.get_attribute("value")
        print(f'Login input text after input syl_wit: {login_input_element_value}')

        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element_enabled_property = login_next_button_element.get_property('enabled')
        print(f'If boolean True?: {login_next_button_element_enabled_property == True}')

        login_input_element.clear()
        print(f'Login input text after cleaning: {login_input_element_text}')