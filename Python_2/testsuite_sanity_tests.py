import unittest

from lost_hat_login_page_tests import LostHatLoginPageTests
from lost_hat_front_page_tests import LostHatFrontPageTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    # test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LostHatLoginPageTests('test_correct_login')))
    test_suite.addTest(LostHatLoginPageTests('test_correct_login'))
    test_suite.addTest(LostHatLoginPageTests('test_sanity_search_on_main_page'))
    test_suite.addTest(LostHatLoginPageTests('test_sanity_search_for_on_main_page'))
    test_suite.addTest(LostHatFrontPageTests('test_sanity_all_products_have_price_in_pln'))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_suite())
