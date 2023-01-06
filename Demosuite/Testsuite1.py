import unittest
from testcal import my_Test
def my_suite():
    suite=unittest.TestSuite()
    r=unittest.TestResult()
    suite.addTests(unittest.makeSuite(my_Test))
    runner=unittest.TextTestRunner(verbosity=1)
    print(runner.run(suite))
my_suite()