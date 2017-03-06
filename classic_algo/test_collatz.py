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

if __name__ == '__main__':
    unittest.main()