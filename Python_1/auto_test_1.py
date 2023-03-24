from selenium import webdriver

from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(r'C:\TestFiles\New_driver\chromedriver.exe'))
driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
#driver.get('https://demobank.jaktestowac.pl/logowanie_prod.html')
title = driver.title
print(title)
assert 'Demobank - Bankowość Internetowa - Logowanie' == title

driver.quit()
