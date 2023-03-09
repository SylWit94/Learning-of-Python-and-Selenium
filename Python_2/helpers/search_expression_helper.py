import time

from selenium.webdriver.common.by import By


def search_element(driver, search_expression):
    """Input value into search element box and search

    :param driver: webdriver instance
    :param search_expression: expression that we want to insert into search box
    :return: None
    """
    # finding search element box and sending value
    search_element = driver.find_element(By.XPATH, '//*[@id="search_widget"]//*[@placeholder="Search our catalog"]')
    search_element.send_keys(search_expression)
    time.sleep(2)

    magnifier_element = driver.find_element(By.XPATH, '//*[@id="search_widget"]/form/button/i')
    magnifier_element.click()
    time.sleep(2)