from solution import filter_array
### test cases
import unittest

class TestFilterArrayFunction(unittest.TestCase):
    """
    This test class contains test cases for the filter_array function.
    Each test case checks the function against a specific scenario.
    """

    def test_no_elements(self):
        """
        Test case where the input array is empty.
        Expected result: An empty array.
        """
        self.assertEqual(filter_array([]), [])

    def test_all_greater_than_five(self):
        """
        Test case where all elements in the input array are greater than 5.
        Expected result: The same elements incremented by 1.
        """
        self.assertEqual(filter_array([6, 7, 8]), [7, 8, 9])

    def test_all_less_than_five(self):
        """
        Test case where all elements in the input array are less than or equal to 5.
        Expected result: The same elements without any changes.
        """
        self.assertEqual(filter_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_mixed_elements(self):
        """
        Test case where the input array contains a mix of elements greater than 5, less than or equal to 5, and zeros.
        Expected result: Elements greater than 5 incremented by 1 and zeros removed.
        """
        self.assertEqual(filter_array([0, 6, 0, 7, 5, 8, 0]), [7, 8, 9])

    def test_single_zero(self):
        """
        Test case where the input array contains only one zero.
        Expected result: An empty array since zeros are removed.
        """
        self.assertEqual(filter_array([0]), [])

    def test_single_element_greater_than_five(self):
        """
        Test case where the input array contains only one element greater than 5.
        Expected result: The element incremented by 1.
        """
        self.assertEqual(filter_array([6]), [7])  # Modified output

if __name__ == '__main__':
    unittest.main()
