import unittest
from primes import *

class TestPrimes(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(29))

    def test_next_prime(self):
        self.assertEqual(next_prime(1), 2)
        self.assertEqual(next_prime(2), 3)
        self.assertEqual(next_prime(10), 11)

if __name__ == '__main__':
    unittest.main()
