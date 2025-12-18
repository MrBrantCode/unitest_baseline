from solution import min_and_max
### test cases
import unittest

class TestMinMaxFunction(unittest.TestCase):
    """
    Test class for the min_and_max function.
    
    This class contains several test methods to ensure the min_and_max function works correctly.
    """

    def test_single_element(self):
        """
        Test case for a list with a single element.
        
        Ensures that the function correctly handles a list with only one element.
        """
        self.assertEqual(min_and_max([5]), (5, 5))

    def test_positive_numbers(self):
        """
        Test case for a list with positive numbers.
        
        Ensures that the function correctly identifies the minimum and maximum values in a list of positive numbers.
        """
        self.assertEqual(min_and_max([3, 1, 2, 4, 5]), (1, 5))

    def test_negative_numbers(self):
        """
        Test case for a list with negative numbers.
        
        Ensures that the function correctly identifies the minimum and maximum values in a list of negative numbers.
        """
        self.assertEqual(min_and_max([-3, -1, -2, -4, -5]), (-5, -1))

    def test_mixed_numbers(self):
        """
        Test case for a list with both positive and negative numbers.
        
        Ensures that the function correctly identifies the minimum and maximum values in a list with mixed positive and negative numbers.
        """
        self.assertEqual(min_and_max([-3, 1, -2, 4, -5]), (-5, 4))

    def test_duplicate_values(self):
        """
        Test case for a list with duplicate values.
        
        Ensures that the function correctly handles lists with duplicate values.
        """
        self.assertEqual(min_and_max([3, 3, 3, 3, 3]), (3, 3))  # Modified output

    def test_large_list(self):
        """
        Test case for a large list of numbers.
        
        Ensures that the function can handle a larger list of numbers without performance issues.
        """
        self.assertEqual(min_and_max(list(range(10000))), (0, 9999))  # Modified output

if __name__ == '__main__':
    unittest.main()
