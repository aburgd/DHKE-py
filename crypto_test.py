"""tests crypto.py using unittest"""
import unittest
import crypto

class CryptoTestCases(unittest.TestCase):
    """tests crypto.py using unittest"""
    def test_number_generation(self):
        """tests crypto.generate() and tests for correct type returned"""
        self.assertIs(int, type(crypto.generate()))
        self.assertIs(int, type(crypto.generate()))


    def test_aks(self):
        """tests crypto.aks(n) with four different ints"""
        self.assertTrue(crypto.aks(5)) # prime
        self.assertTrue(crypto.aks(1915757)) # prime
        self.assertFalse(crypto.aks(9)) # composite
        self.assertFalse(crypto.aks(12705198)) # composite


if __name__ == '__main__':
    unittest.main()
