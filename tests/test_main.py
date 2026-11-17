import unittest
from finder import findMaxNumber

class testMaxNumber(unittest.TestCase):

    def test_Max_Number(self):
        self.assertEqual(findMaxNumber([1,2,3,4,5]), 5)

    def test_Max_Number_Multiple_Digits(self):
        self.assertEqual(findMaxNumber([10,11,12,14,13,6,170]), 170)

if __name__ == '__main__':
    unittest.main()