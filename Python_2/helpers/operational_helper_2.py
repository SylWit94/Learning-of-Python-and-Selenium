from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def visibility_of_element_wait(driver, xpath, timeout=10):

    timeout_message = f'Element for xpath: {xpath} and url: {driver.current_url} not found in {timeout} seconds'
    locator = (By.XPATH, xpath)
    element_located = ec.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, timeout)
    return wait.until(element_located, timeout_message)