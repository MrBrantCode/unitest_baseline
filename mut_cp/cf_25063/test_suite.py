from solution import reverse_array
### test cases
import unittest

class TestReverseArray(unittest.TestCase):
    """
    This class contains test cases for the reverse_array function.
    """

    def test_empty_list(self):
        """
        Test if an empty list is returned when an empty list is passed.
        """
        self.assertEqual(reverse_array([]), [])

    def test_single_element(self):
        """
        Test if a single-element list is returned unchanged.
        """
        self.assertEqual(reverse_array([42]), [42])

    def test_multiple_elements(self):
        """
        Test if a list with multiple elements is correctly reversed.
        """
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_negative_numbers(self):
        """
        Test if a list containing negative numbers is correctly reversed.
        """
        self.assertEqual(reverse_array([-1, -2, -3]), [-3, -2, -1])

    def test_mixed_numbers(self):
        """
        Test if a list containing both positive and negative numbers is correctly reversed.
        """
        self.assertEqual(reverse_array([1, -2, 3, -4, 5]), [5, -4, 3, -2, 1])

if __name__ == '__main__':
    unittest.main()
