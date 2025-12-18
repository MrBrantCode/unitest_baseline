from solution import array_processor
# Test cases are provided below.

### test cases
import unittest

class TestArrayProcessor(unittest.TestCase):
    """
    Test cases for the array_processor function.
    """

    def test_only_integers(self):
        """
        Test case with only integer values in the 2D array.
        """
        arr = [[1, 2], [3, 4]]
        expected_output = (10, '', 0)
        self.assertEqual(array_processor(arr), expected_output)

    def test_only_strings(self):
        """
        Test case with only string values in the 2D array.
        """
        arr = [['hello', 'world'], ['python', 'unittest']]
        expected_output = (0, 'helloworldpythonunittest', 0)
        self.assertEqual(array_processor(arr), expected_output)

    def test_only_booleans(self):
        """
        Test case with only boolean values in the 2D array.
        """
        arr = [[True, False], [True, True]]
        expected_output = (3, '', 0)
        self.assertEqual(array_processor(arr), expected_output)

    def test_mixed_types(self):
        """
        Test case with a mix of integers, strings, and booleans in the 2D array.
        """
        arr = [[1, 'a', True], [2, 'b', False], [3, 'c', True]]
        expected_output = (6, 'abc', 2)
        self.assertEqual(array_processor(arr), expected_output)

    def test_empty_array(self):
        """
        Test case with an empty 2D array.
        """
        arr = []
        expected_output = (0, '', 0)
        self.assertEqual(array_processor(arr), expected_output)  # Modified output

    def test_single_element_subarrays(self):
        """
        Test case with single-element sub-arrays.
        """
        arr = [[1], ['hello'], [True]]
        expected_output = (2, 'hello', 1)
        self.assertEqual(array_processor(arr), expected_output)  # Modified output

if __name__ == '__main__':
    unittest.main()
