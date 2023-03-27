import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from helpers import operational_helper_2 as oh2


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r"C:\TestFiles\New_driver\chromedriver.exe"))

    def test_demo_login(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Konta', title,
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_pulpit(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title,
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title,
                         f'Expected title differ from actual for page url: {url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


class LoginPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r"C:\TestFiles\New_driver\chromedriver.exe"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_exact_text_for_login_form_header(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_form_header_element = driver.find_element(By.XPATH, '//*[@id="login_form"]/h1')
        login_form_header_text = login_form_header_element.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', login_form_header_text,
                         f'Expected title differ from actual title for page url: {url}')

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

    def test_display_error_message_when_user_submit_less_than_8_signs(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_form_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_text = '1234567'
        login_form_input_element.send_keys(login_text)
        hint_button_element = driver.find_element(By.XPATH,
                                                  '//*[@id="login_id_container"]//*[@class="i-hint-white tooltip widget-info"]')
        hint_button_element.click()
        warning_message_element = driver.find_element(By.XPATH, '//*[@class="error"]')
        warning_message_text = warning_message_element.text
        self.assertEqual('identyfikator ma min. 8 znaków', warning_message_text,
                         f'Expected warning message differ from actual one for url: {url}')

    def test_button_dalej_respond_when_enters_8_signs_id(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_form_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_form_input_element.clear()
        login_text = '12345678'
        login_form_input_element.send_keys(login_text)
        login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        login_next_button_element.click()
        # time.sleep(3)
        login_next_button_xpath = '//*[@id="login_next"]'
        login_next_button_element = oh2.visibility_of_element_wait(driver, login_next_button_xpath)
        # login_next_button_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        new_login_button_text = login_next_button_element.text
        self.assertEqual('dalej', new_login_button_text,
                         f'Expected login button text: dalej , differ from actual {new_login_button_text}')

    # Teraz Ty 1
    def test_correct_popup_text(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_reminder_element = driver.find_element(By.XPATH, '//*[@id="ident_rem"]')
        login_reminder_element.click()
        # time.sleep(3)
        popup_text_xpath = '//*[@class="shadowbox-content contact-popup"]/div/h2'
        popup_text_element = oh2.visibility_of_element_wait(driver, popup_text_xpath)
        # popup_text_element = driver.find_element(By.XPATH, '//*[@class="shadowbox-content contact-popup"]/div/h2')
        popup_text_element_text = popup_text_element.text
        popup_text_element_close_button = driver.find_element(By.XPATH, '//*[@id="shadowbox"]/div/i')
        popup_text_element_close_button.click()
        self.assertEqual('ta funkcja jest niedostępna', popup_text_element_text,
                         f'Expected login button text differ from actual: {popup_text_element_text}')

    # Teraz Ty 2
    def test_correct_login_from_login_etap2(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        driver.get(url)
        # finding login input box and sending value
        login_input_element = driver.find_element(By.XPATH, '//*[@id="login_id"]')
        login_input_element.send_keys('kocur131')
        # finding login password box and sending value
        password_input_element = driver.find_element(By.XPATH, '//*[@id="login_password"]')
        password_input_element.send_keys('123456789')
        # finding button 'zaloguj'
        button_next_element = driver.find_element(By.XPATH, '//*[@id="login_next"]')
        button_next_element.click()
        # time.sleep(3)
        messages_element_xpath = '//*[@id="show_messages"]'
        messages_element = oh2.visibility_of_element_wait(driver, messages_element_xpath)
        # finding unique element to check if login was successful
        # messages_element = driver.find_element(By.XPATH, '//*[@id="show_messages"]')
        messages_element_text = messages_element.text
        self.assertEqual('Brak wiadomości', messages_element_text,
                         f'Expected login button text differ from actual: {messages_element_text}')


class ContactUsPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_contact_us_form_header(self):
        expected_text = 'CONTACT US'
        contact_us_page_url = 'https://autodemo.testoneo.com/en/contact-us'
        driver = self.driver
        driver.get(contact_us_page_url)
        header_xpath = '//*[@id="content"]//*[@class="col-md-9 col-md-offset-3"]'
        header_element = driver.find_element(By.XPATH, header_xpath)
        header_element_text = header_element.text
        print(header_element_text)

        self.assertEqual(expected_text, header_element_text,
                         f'Expected text differ from actual {header_element_text} for url {contact_us_page_url}')

    def test_contact_us_form_with_empty_email_element(self):
        expected_warning_text = 'Invalid email address.'
        contact_us_page_url = 'https://autodemo.testoneo.com/en/contact-us'
        driver = self.driver
        driver.get(contact_us_page_url)
        send_button_xpath = '//*[@id="content"]//*[@type="submit"]'
        send_button_element = driver.find_element(By.XPATH, send_button_xpath)
        send_button_element.click()

        warning_element_xpath = '//*[@id="content"]//*[@class="col-xs-12 alert alert-danger"]'
        locator = (By.XPATH, warning_element_xpath)
        warning_element = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(locator), f'Element not found')

        self.assertEqual(expected_warning_text, warning_element.text)
