import unittest
def mul(a,b):
    return a*b
class my_Test(unittest.TestCase):
    def test1(self):
        a=10
        b=20
        r=mul(a,b)
        self.assertEqual(r,200)
    def test2(self):
        a=-10
        b=20
        r=mul(a,b)
        self.assertEqual(r,-200)
    def test3(self):
        a=-20
        b=-20
        r=mul(a,b)
        self.assertEqual(r,400)
    def test4(self):
        a=56
        b=20
        r=mul(a,b)
        self.assertEqual(r,1120)
    def test5(self):
        a=16
        b=26
        r=mul(a,b)
        self.assertNotEqual(r,41)
