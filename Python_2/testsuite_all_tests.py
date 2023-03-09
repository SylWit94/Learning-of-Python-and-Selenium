import unittest

from lost_hat_smoke_tests_alternative_solution import LostHatSmokeTests
from lost_hat_front_page_tests import LostHatFrontPageTests
from lost_hat_product_page_tests import LostHatProductPageTests
from lost_hat_login_page_tests import LostHatLoginPageTests


def full_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LostHatSmokeTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LostHatFrontPageTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LostHatProductPageTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LostHatLoginPageTests))
    return test_suite


# This line is added to run tests with Allure
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())

