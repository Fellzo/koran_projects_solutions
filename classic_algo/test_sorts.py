import unittest

from . import algorithms


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