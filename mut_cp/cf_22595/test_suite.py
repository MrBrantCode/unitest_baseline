from solution import is_unique_list
### test cases
import unittest

class TestIsUniqueList(unittest.TestCase):
    """
    Test cases for the is_unique_list function.
    """

    def test_empty_list(self):
        """
        Test an empty list.
        """
        self.assertTrue(is_unique_list([]))

    def test_single_element_list(self):
        """
        Test a list with a single element.
        """
        self.assertTrue(is_unique_list([1]))

    def test_unique_elements(self):
        """
        Test a list with unique elements.
        """
        self.assertTrue(is_unique_list([1, 2, 3]))

    def test_duplicate_elements(self):
        """
        Test a list with duplicate elements.
        """
        self.assertFalse(is_unique_list([1, 2, 2]))

    def test_nested_lists(self):
        """
        Test a list containing nested lists.
        """
        self.assertTrue(is_unique_list([[1], [2], [3]]))
        self.assertFalse(is_unique_list([[1], [2], [2]]))

    def test_nested_dicts(self):
        """
        Test a list containing nested dictionaries.
        """
        self.assertTrue(is_unique_list([{'a': 1}, {'b': 2}, {'c': 3}]))
        self.assertFalse(is_unique_list([{'a': 1}, {'b': 2}, {'b': 2}]))

    def test_mixed_types(self):
        """
        Test a list with mixed types including lists and dictionaries.
        """
        self.assertTrue(is_unique_list([1, [2], {'a': 3}]))
        self.assertFalse(is_unique_list([1, [2], [2]]))  # Modified here

    def test_complex_structure(self):
        """
        Test a complex structure with nested lists and dictionaries.
        """
        self.assertTrue(is_unique_list([{'a': 1, 'b': [2]}, {'c': 3}]))
        self.assertFalse(is_unique_list([{'a': 1, 'b': [2]}, {'c': 3, 'd': [2]}]))  # Modified here

if __name__ == '__main__':
    unittest.main()
