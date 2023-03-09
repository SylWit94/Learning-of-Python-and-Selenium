import unittest

from lost_hat_smoke_tests_alternative_solution import LostHatSmokeTests


def smoke_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LostHatSmokeTests))
    # test_suite.addTest(makeSuite(LostHatSmokeTests)) return error
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())



