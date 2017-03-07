import unittest
from primegen import prime
class Testprimegen(unittest.TestCase):
    def test_number_is_positive(self):
        self.assertFalse(prime(-1))
    def test_number_equal_two(self):
        self.assertTrue(prime(2))
    def test_number_isnot_two_and_one(self):
        self.assertTrue(prime(2))
    def test_number_equal_one(self):
        self.assertFalse(prime(1))
    def test_number_modulus_i_equal_zero(self):
        self.assertFalse(prime(10))
    def test_number_modulus_i_not_equal_zero(self):
        self.assertTrue(prime(11))

if __name__=="__main__":
    unittest.main()
