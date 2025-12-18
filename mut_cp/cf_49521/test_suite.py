from solution import binary_search
### test cases
import unittest

class TestBinarySearch(unittest.TestCase):
    def test_ascending_order(self):
        # Test case for an ascending order list with duplicates
        lst = [1, 2, 3, 4, 5, 5, 6]
        val = 5
        self.assertEqual(binary_search(lst, val), 4)

    def test_descending_order(self):
        # Test case for a descending order list with duplicates
        lst = [6, 5, 5, 4, 3, 2, 1]
        val = 5
        self.assertEqual(binary_search(lst, val), 1)

    def test_value_not_found(self):
        # Test case where the value is not present in the list
        lst = [1, 2, 3, 4, 5]
        val = 6
        self.assertEqual(binary_search(lst, val), -1)

    def test_single_element_list(self):
        # Test case for a list with a single element
        lst = [1]
        val = 1
        self.assertEqual(binary_search(lst, val), 0)

    def test_empty_list(self):
        # Test case for an empty list
        lst = []
        val = 1
        self.assertEqual(binary_search(lst, val), -1)

    def test_duplicate_at_start(self):
        # Test case for a list with duplicates at the start
        lst = [1, 1, 1, 2, 3, 4, 5]
        val = 1
        self.assertEqual(binary_search(lst, val), 0)

    def test_duplicate_at_end(self):
        # Test case for a list with duplicates at the end
        lst = [1, 2, 3, 4, 5, 5, 5]
        val = 5
        self.assertEqual(binary_search(lst, val), 4)  # Modified output

    def test_all_elements_same(self):
        # Test case for a list where all elements are the same
        lst = [1, 1, 1, 1, 1]
        val = 1
        self.assertEqual(binary_search(lst, val), 0)  # Modified output

if __name__ == '__main__':
    unittest.main()
