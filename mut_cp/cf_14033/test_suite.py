from solution import check_lists
### Test Cases
import unittest

class TestCheckListsFunction(unittest.TestCase):
    """
    This class contains test cases for the check_lists function.
    Each test case checks the function against different scenarios to ensure its correctness.
    """

    def test_identical_lists(self):
        """
        Test case where both lists are identical.
        Expected result: True
        """
        self.assertTrue(check_lists(['a', 'b', 'c'], ['a', 'b', 'c']))

    def test_different_order(self):
        """
        Test case where the lists contain the same elements but in a different order.
        Expected result: True
        """
        self.assertTrue(check_lists(['c', 'b', 'a'], ['a', 'b', 'c']))

    def test_different_elements(self):
        """
        Test case where the lists contain different elements.
        Expected result: False
        """
        self.assertFalse(check_lists(['a', 'b', 'c'], ['d', 'e', 'f']))

    def test_empty_lists(self):
        """
        Test case where both lists are empty.
        Expected result: True
        """
        self.assertTrue(check_lists([], []))

    def test_one_empty_list(self):
        """
        Test case where one list is empty and the other is not.
        Expected result: False
        """
        self.assertFalse(check_lists([], ['a', 'b', 'c']))
        self.assertFalse(check_lists(['a', 'b', 'c'], []))

    def test_duplicate_elements(self):
        """
        Test case where the lists contain duplicate elements.
        Expected result: True
        """
        self.assertTrue(check_lists(['a', 'b', 'b'], ['b', 'b', 'a']))

    def test_large_lists(self):
        """
        Test case with large lists (maximum allowed size).
        Expected result: True or False depending on the content of the lists.
        """
        # Create two identical lists of maximum size
        list1 = ['a'] * 100
        list2 = ['a'] * 100
        self.assertTrue(check_lists(list1, list2))
        
        # Create two different lists of maximum size
        list1 = ['a'] * 50 + ['b'] * 50
        list2 = ['a'] * 50 + ['c'] * 50
        self.assertFalse(check_lists(list1, list2))  # Modified output

if __name__ == '__main__':
    unittest.main()
