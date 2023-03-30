from selenium.webdriver.support.events import AbstractEventListener
import time


class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_path = rf"C:\Users\Opti\PycharmProjects\pythonProject\demo_tests_2\test_result_screenshots\driver_exception_{time.time()}.png"
        driver.get_screenshot_as_file(screenshot_path)
        print(f'Screenshot saved as {screenshot_path}')
