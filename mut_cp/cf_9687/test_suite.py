from solution import counting_sort
### test cases
import unittest

class TestCountingSort(unittest.TestCase):
    def test_empty_list(self):
        # Test case for an empty list
        self.assertEqual(counting_sort([]), [])

    def test_single_element(self):
        # Test case for a list with a single element
        self.assertEqual(counting_sort([5]), [5])

    def test_sorted_list(self):
        # Test case for a list that is already sorted
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        # Test case for a list that is sorted in reverse order
        self.assertEqual(counting_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        # Test case for a list that is unsorted
        self.assertEqual(counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_duplicate_values(self):
        # Test case for a list with duplicate values
        self.assertEqual(counting_sort([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_large_range(self):
        # Test case for a list with a large range of values
        self.assertEqual(counting_sort([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])  # Modified output

    def test_mixed_values(self):
        # Test case for a list with mixed values
        self.assertEqual(counting_sort([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # Modified output

if __name__ == '__main__':
    unittest.main()
