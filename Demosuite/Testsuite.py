import unittest
from Test_caes2 import my_Test
def my_suite():
    suite=unittest.TestSuite()
    r=unittest.TestResult()
    suite.addTests(unittest.makeSuite(my_Test))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()