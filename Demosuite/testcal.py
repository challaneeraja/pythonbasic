import unittest
def count_days(n):
    if n in [1,3,5,7,8,10,12]:
        return 31
    elif n in [4,6,9,11]:
        return 30
    else:
        return 28
def login(un,pa):
    if(un=="hcluser" and pa=="1234"):
        return 1
    else:
        return 0
class my_Test(unittest.TestCase):
    def test(self):
        n=4
        r=count_days(n)
        self.assertEqual(r,30)
    def test1(self):
        un="hcluser"
        pa="1234"
        r=login(un,pa)
        self.assertEqual(r,1)
