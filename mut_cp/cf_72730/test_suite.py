from solution import min_periods
### test cases
import unittest

class TestMinPeriods(unittest.TestCase):
    def test_no_overlap(self):
        # Test case with no overlapping time periods
        intervals = [[1, 3], [4, 6]]
        self.assertEqual(min_periods(intervals), 2)

    def test_partial_overlap(self):
        # Test case with partially overlapping time periods
        intervals = [[1, 4], [5, 7]]
        self.assertEqual(min_periods(intervals), 2)

    def test_full_overlap(self):
        # Test case with fully overlapping time periods
        intervals = [[1, 10], [2, 9]]
        self.assertEqual(min_periods(intervals), 1)

    def test_unsorted_input(self):
        # Test case with unsorted input
        intervals = [[4, 6], [1, 3]]
        self.assertEqual(min_periods(intervals), 2)

    def test_single_period(self):
        # Test case with a single time period
        intervals = [[1, 5]]
        self.assertEqual(min_periods(intervals), 1)

    def test_empty_input(self):
        # Test case with an empty list
        intervals = []
        self.assertEqual(min_periods(intervals), 0)  # Modified output

    def test_overlapping_with_gap(self):
        # Test case with overlapping time periods and a gap in between
        intervals = [[1, 3], [4, 6], [7, 9]]
        self.assertEqual(min_periods(intervals), 3)

    def test_consecutive_intervals(self):
        # Test case with consecutive time periods
        intervals = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(min_periods(intervals), 1)  # Modified output

if __name__ == '__main__':
    unittest.main()
