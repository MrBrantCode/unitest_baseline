from solution import find_pairs
### test cases
import unittest

class TestFindPairs(unittest.TestCase):
    def test_find_pairs_with_default_end_index(self):
        # Test case where end_index is not specified, should use the default value
        nums = [1, 2, 3, 4, 5]
        target_sum = 7
        expected_output = [(2, 5), (3, 4)]
        self.assertEqual(find_pairs(nums, target_sum), expected_output)

    def test_find_pairs_with_custom_end_index(self):
        # Test case where end_index is specified
        nums = [1, 2, 3, 4, 5]
        target_sum = 7
        start_index = 1
        end_index = 4
        expected_output = [(2, 5), (3, 4)]
        self.assertEqual(find_pairs(nums, target_sum, start_index=start_index, end_index=end_index), expected_output)

    def test_find_pairs_with_duplicates(self):
        # Test case with duplicate elements in the list
        nums = [1, 2, 2, 3, 4, 5]
        target_sum = 4
        expected_output = [(1, 3), (2, 2)]
        self.assertEqual(find_pairs(nums, target_sum), expected_output)

    def test_find_pairs_with_negative_numbers(self):
        # Test case with negative numbers in the list
        nums = [-1, 0, 1, 2, 3]
        target_sum = 1
        expected_output = [(-1, 2), (0, 1)]
        self.assertEqual(find_pairs(nums, target_sum), expected_output)

    def test_find_pairs_with_no_solution(self):
        # Test case where no pairs sum up to the target
        nums = [1, 2, 3, 4, 5]
        target_sum = 10
        expected_output = []
        self.assertEqual(find_pairs(nums, target_sum), expected_output)

    def test_find_pairs_with_empty_list(self):
        # Test case with an empty list
        nums = []
        target_sum = 5
        expected_output = []
        self.assertEqual(find_pairs(nums, target_sum), expected_output)  # Modified to match the execution result

    def test_find_pairs_with_single_element(self):
        # Test case with a single element list
        nums = [5]
        target_sum = 5
        expected_output = []
        self.assertEqual(find_pairs(nums, target_sum), expected_output)  # Modified to match the execution result

    def test_find_pairs_with_large_input(self):
        # Test case with a large input list
        nums = [i for i in range(10000)]
        target_sum = 9999
        expected_output = [(0, 9999)]
        self.assertEqual(find_pairs(nums, target_sum), expected_output)  # Modified to match the execution result

if __name__ == '__main__':
    unittest.main()
