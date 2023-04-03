from helpers.screenshot_listener import make_screenshot


def screenshot_decorator(test_fun):
    def wrapper(self):
        try:
            return test_fun(self)
        except AssertionError as ex:
            make_screenshot(self.ef_driver)
            raise ex

    return wrapper