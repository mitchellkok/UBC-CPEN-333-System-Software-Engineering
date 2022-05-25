import unittest #importing the test framework class
from demo import Arithmetic

class Test(unittest.TestCase):
    def test_add(self):
        a, b = -1, 15
        self.assertEqual(Arithmetic.add(a, b), a+b)

    def test_add1(self):
        a, b = -1, 15
        self.assertEqual(Arithmetic.add(a, b), a+b-1)

    def test_subtract(self):
        a, b = -1, 15
        self.assertEqual(Arithmetic.subtract(a, b), a-b)
    
    def test_subtract1(self):
        a, b = -1, 15
        self.assertEqual(Arithmetic.subtract(a, b), a-b-1)

if __name__ == '__main__':
    unittest.main() 