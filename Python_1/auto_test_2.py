import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from selenium.webdriver.chrome.service import Service
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))

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
