import unittest
def lon(l):
    for each in l:
        return (max(l))
class my_Test(unittest.TestCase):
    def test(self):
        l=[29,3,20,71,713]
        r=lon(l)
        self.assertEqual(r,713)
