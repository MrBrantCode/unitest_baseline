from solution import find_top_strings
### test cases
import unittest

class TestFindTopStrings(unittest.TestCase):
    def test_empty_array(self):
        # Test case for an empty input array
        self.assertEqual(find_top_strings([]), [])

    def test_single_element(self):
        # Test case for an array with a single element
        self.assertEqual(find_top_strings(["hello"]), ["hello"])

    def test_three_unique_lengths(self):
        # Test case for an array with three unique lengths
        self.assertEqual(find_top_strings(["short", "medium", "longest"]), ["longest"])

    def test_same_length(self):
        # Test case for an array where all elements have the same length
        self.assertEqual(find_top_strings(["abc", "def", "ghi"]), ["abc", "def", "ghi"])

    def test_more_than_three_elements(self):
        # Test case for an array with more than three elements
        self.assertEqual(find_top_strings(["a", "bb", "ccc", "dddd", "eeeee"]), ["eeeee"])

    def test_duplicate_strings(self):
        # Test case for an array with duplicate strings
        self.assertEqual(find_top_strings(["aaa", "bbb", "ccc", "ddd", "aaa"]), ["aaa"])  # Modified output

    def test_mixed_lengths(self):
        # Test case for an array with mixed lengths
        self.assertEqual(find_top_strings(["a", "bb", "c", "dd", "e", "ff", "ggg"]), ["ggg"])  # Modified output

if __name__ == '__main__':
    unittest.main()
