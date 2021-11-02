import unittest
from super_algos import *


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(-1, find_min([]))
        self.assertEqual(-1, find_min([0, 1, 2, "3", 4]))
        self.assertEqual(-1, find_min([0, 1, -2, 3, ""]))
        self.assertEqual(-1, find_min([0, 1, 2, range(100), 4]))
        self.assertEqual(-1, find_min([0, 1, 2, dict(a="u"), 4]))
        self.assertEqual(0, find_min([2, 4, 1, 3, 0]))
        self.assertEqual(0, find_min([2, 4, 0, 3, 1]))
        self.assertEqual(-2, find_min([0, 1, -2, 3, 4]))

    def test_sum_all(self):
        self.assertEqual(-1, sum_all([0, 1, -2, 3, ""]))
        self.assertEqual(-1, sum_all([0, 1, 2, range(100), 4]))
        self.assertEqual(-1, sum_all([0, 1, 2, dict(a="u"), 4]))
        self.assertEqual(-1, sum_all([]))
        self.assertEqual(-1, sum_all([0, 1, 2, "3", 4]))
        self.assertEqual(15, sum_all([1, 2, 3, 4, 5]))
        self.assertEqual(4950, sum_all([i for i in range(100)]))

    def test_find_all_possible_strings(self):
        self.assertEqual(
            ["xxx", "xxy", "xyx", "xyy", "yxx", "yxy", "yyx", "yyy"],
            find_possible_strings(["x", "y"], 3),
        )
        self.assertEqual(["aa", "ab", "ba", "bb"],
                         find_possible_strings(["a", "b"], 2))
        self.assertEqual([], find_possible_strings(range(9), 10))
        self.assertEqual([], find_possible_strings(["", "\n"], 3))
