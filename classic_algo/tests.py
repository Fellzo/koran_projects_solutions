import unittest

from . import algorithms


class TestCollatz(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(algorithms.collatz_conjecture(10), 6, "10->5->16->8->4->2->1")

    def test_long_sequence(self):
        self.assertEqual(algorithms.collatz_conjecture(27), 111)

    def test_large_number(self):
        self.assertEqual(algorithms.collatz_conjecture(2382737577286911665266), 2739, "Largest test")

    def test_negative(self):
        self.assertRaises(ValueError, algorithms.collatz_conjecture, -1)


class TestMergeSort(unittest.TestCase):

    def test_simple(self):
        self.assertEqual([1, 4, 8, 8], algorithms.merge_sort([8, 4, 1, 8]))

    def test_empty(self):
        self.assertEqual([], algorithms.merge_sort([]))

    def test_only_negative(self):
        self.assertEqual([-199, -35, -15, -10, -3], algorithms.merge_sort([-3, -10, -199, -35, -15]))

    def test_custom_comparator(self):
        self.assertEqual([1, 3, 7], algorithms.merge_sort([3, 1, 7], lambda x: x - 10))


class TestBubbleSort(unittest.TestCase):

    def test_simple(self):
        self.assertEqual([1, 4, 8, 8], algorithms.bubble_sort([8, 4, 1, 8]))

    def test_empty(self):
        self.assertEqual([], algorithms.bubble_sort([]))

    def test_only_negative(self):
        self.assertEqual([-199, -35, -15, -10, -3], algorithms.bubble_sort([-3, -10, -199, -35, -15]))


class TestEratosthenesSieve(unittest.TestCase):
    def test_simple(self):
        self.assertEqual([2, 3, 5, 7], algorithms.sieve_of_eratosthenes(10))

    def test_no_primes(self):
        self.assertEqual([], algorithms.sieve_of_eratosthenes(1))

    def test_exception(self):
        self.assertRaises(ValueError, algorithms.sieve_of_eratosthenes, -1)


class TestIsPrimeNumber(unittest.TestCase):
    def test_simple_group(self):
        self.assertEqual(True, algorithms.is_prime_number(2))
        self.assertEqual(True, algorithms.is_prime_number(5))
        self.assertEqual(False, algorithms.is_prime_number(1))
        self.assertEqual(False, algorithms.is_prime_number(4))

    def test_big_numbers(self):
        self.assertEqual(True, algorithms.is_prime_number(10 ** 4 + 7))
        self.assertEqual(False, algorithms.is_prime_number(143919))

    def test_exception(self):
        self.assertRaises(ValueError, algorithms.is_prime_number, 0)
        self.assertRaises(ValueError, algorithms.is_prime_number, -131)