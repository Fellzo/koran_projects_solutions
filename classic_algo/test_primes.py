import unittest
from . import algorithms


class TestEratosthenesSieve(unittest.TestCase):
    def test_simple(self):
        self.assertEqual([2, 3, 5, 7], algorithms.sieve_of_eratosthenes(10))

    def test_no_primes(self):
        self.assertEqual([], algorithms.sieve_of_eratosthenes(1))

    def test_exeption(self):
        self.assertRaises(ValueError, algorithms.sieve_of_eratosthenes, -1)


class TestIsPrimeNumber(unittest.TestCase):
    def test_simple_group(self):
        self.assertEqual(True, algorithms.is_prime_number(2))
        self.assertEqual(True, algorithms.is_prime_number(5))
        self.assertEqual(False, algorithms.is_prime_number(1))
        self.assertEqual(False, algorithms.is_prime_number(4))

    def test_big_numbers(self):
        self.assertEqual(True, algorithms.is_prime_number(10 ** 4 + 7))

    def test_exception(self):
        self.assertRaises(ValueError, algorithms.is_prime_number, 0)
        self.assertRaises(ValueError, algorithms.is_prime_number, -131)