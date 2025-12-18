from solution import find_indices_and_average
### test cases
import unittest

class TestFindIndicesAndAverage(unittest.TestCase):
    def test_no_occurrences(self):
        # Test when the target number does not occur in the array
        self.assertEqual(find_indices_and_average(5, [1, 2, 3, 4]), -1)

    def test_single_occurrence(self):
        # Test when the target number occurs only once in the array
        self.assertEqual(find_indices_and_average(3, [1, 2, 3, 4]), 3)

    def test_multiple_occurrences(self):
        # Test when the target number occurs multiple times in the array
        self.assertEqual(find_indices_and_average(2, [1, 2, 2, 3, 2]), 2)

    def test_average_index_not_whole_number(self):
        # Test when the average index is not a whole number
        self.assertEqual(find_indices_and_average(2, [1, 2, 3, 2, 4]), -1)

    def test_average_index_whole_number(self):
        # Test when the average index is a whole number
        self.assertEqual(find_indices_and_average(2, [1, 2, 2, 2, 4]), 2)

    def test_empty_array(self):
        # Test when the array is empty
        self.assertEqual(find_indices_and_average(2, []), -1)  # Modified output

    def test_all_elements_same(self):
        # Test when all elements in the array are the same
        self.assertEqual(find_indices_and_average(2, [2, 2, 2, 2]), 2)  # Modified output

if __name__ == '__main__':
    unittest.main()
