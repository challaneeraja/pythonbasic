import CalcMode as cm
import unittest
print(cm.name)
print(cm.version)
class my_Test(unittest.TestCase):
    def test_add(self):
        r=cm.add_int(10,10)
        self.assertEqual(r,20)
    def test_sub(self):
        r=cm.sub(10,10)
        self.assertEqual(r,0)
    def test_mul(self):
        r=cm.mul(10,10)
        self.assertEqual(r,100)
    def test_div(self):
        r=cm.div(10,10)
        self.assertEqual(r,1)