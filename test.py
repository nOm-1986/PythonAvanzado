""" Testing methods """
import unittest
from palindrome import is_palindrome


class CajaNegraTest(unittest.TestCase):
    
    def test_is_palindrome(self):
        string = 'ana'
        result = is_palindrome(string)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()