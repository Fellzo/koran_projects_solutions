import unittest
from . import nums


class TestFactorial(unittest.TestCase):

    def test_simple_group(self):
        self.assertEqual(1, nums.factorial(0))
        self.assertEqual(1, nums.factorial(1))
        self.assertEqual(2, nums.factorial(2))
        self.assertEqual(120, nums.factorial(5))

    def test_exception(self):
        self.assertRaises(ValueError, nums.factorial, -1)


class TestConverter(unittest.TestCase):

    def test_simple_group(self):
        self.assertEqual('111', nums.converter('7', 10, 2))
        self.assertEqual('7', nums.converter('111', 2, 10))
        self.assertEqual('F', nums.converter('15', 10, 16))

    def test_hard_group(self):
        self.assertEqual('FFFF', nums.converter('1223223', 6, 16))
        self.assertEqual('311300', nums.converter('14883', 9, 5))
        self.assertEqual('-22', nums.converter('-211', 3, 10))

    def test_exception(self):
        self.assertRaises(ValueError, nums.converter, '', 35, -1)
        self.assertRaises(ValueError, nums.converter, '1431', 3, 10)
        self.assertRaises(ValueError, nums.converter, '()31', 3, 10)
        self.assertRaises(ValueError, nums.converter, 'F31', 3, 10)
        self.assertRaises(ValueError, nums.converter, '', 3, 10)


class TestFibonacci(unittest.TestCase):
    def test_simple(self):
        self.assertEqual([], nums.fibonacci_sequence(0))
        self.assertEqual([0], nums.fibonacci_sequence(1))
        self.assertEqual([0, 1], nums.fibonacci_sequence(2))
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], nums.fibonacci_sequence(10))

    def test_exception(self):
        self.assertRaises(ValueError, nums.fibonacci_sequence, -1)


class TestFactorization(unittest.TestCase):
    def test_simple(self):
        self.assertEqual([2, 2, 2, 2], nums.factorization(16))
        self.assertEqual([2, 3, 3], nums.factorization(18))
        self.assertEqual([2, 3, 5], nums.factorization(30))

    def test_exception(self):
        self.assertRaises(ValueError, nums.factorization, -1)