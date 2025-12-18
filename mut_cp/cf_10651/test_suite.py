from solution import check_duplicates
### test cases
import unittest

class TestCheckDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        # Test case where there are no duplicates in the array
        self.assertFalse(check_duplicates([1, 2, 3, 4, 5]))

    def test_with_duplicates(self):
        # Test case where there are duplicates in the array
        self.assertTrue(check_duplicates([1, 2, 2, 3, 4]))

    def test_empty_array(self):
        # Test case with an empty array
        self.assertFalse(check_duplicates([]))

    def test_single_element(self):
        # Test case with a single element array
        self.assertFalse(check_duplicates([42]))

    def test_length_exceeds_100(self):
        # Test case where the length of the array exceeds 100
        arr = list(range(101))
        self.assertFalse(check_duplicates(arr))

    def test_not_sorted(self):
        # Test case where the array is not sorted in ascending order
        self.assertFalse(check_duplicates([1, 3, 2, 4, 5]))

    def test_mixed_cases(self):
        # Test case with mixed conditions (length <= 100, sorted, and duplicates)
        self.assertTrue(check_duplicates([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))  # This should fail due to length exceeding 100

# Note: The above test case 'test_mixed_cases' will fail because the length of the array exceeds 100.
# To make it pass, you would need to modify the array to be within the specified length limit.  # Modified to be within the limit
        self.assertTrue(check_duplicates([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 100]))  # This should fail due to duplicate element 100

if __name__ == '__main__':
    unittest.main()
