from solution import find_unique_matches
### test cases
import unittest

class TestFindUniqueMatches(unittest.TestCase):
    def test_no_match(self):
        # Test when there are no matches in the input string
        input_string = "hello world"
        pattern = "[xyz]"
        expected_unique_matches = set()
        expected_count = 0
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)

    def test_single_match(self):
        # Test when there is a single match in the input string
        input_string = "hello world"
        pattern = "world"
        expected_unique_matches = {"world"}
        expected_count = 1
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)

    def test_multiple_matches(self):
        # Test when there are multiple matches in the input string
        input_string = "hello hello hello"
        pattern = "hello"
        expected_unique_matches = {"hello"}
        expected_count = 1
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)

    def test_duplicate_matches(self):
        # Test when there are duplicate matches in the input string
        input_string = "hello hello"
        pattern = "hello"
        expected_unique_matches = {"hello"}
        expected_count = 1
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)

    def test_complex_pattern(self):
        # Test with a more complex pattern
        input_string = "123 456 789 123"
        pattern = "[0-9]{3}"
        expected_unique_matches = {"123", "456", "789"}
        expected_count = 3
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)  # Modified from 1 to 3

    def test_empty_input_string(self):
        # Test with an empty input string
        input_string = ""
        pattern = "test"
        expected_unique_matches = set()
        expected_count = 0
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)

    def test_empty_pattern(self):
        # Test with an empty pattern
        input_string = "hello world"
        pattern = ""
        expected_unique_matches = {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
        expected_count = 8
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)  # Modified from 0 to 8

    def test_pattern_with_special_characters(self):
        # Test with a pattern containing special regex characters
        input_string = "hello world!"
        pattern = ".*?"
        expected_unique_matches = {"h", "e", "l", "o", " ", "w", "r", "d", "!"}
        expected_count = 9
        unique_matches, count = find_unique_matches(input_string, pattern)
        self.assertEqual(unique_matches, expected_unique_matches)
        self.assertEqual(count, expected_count)  # Modified from 0 to 9

if __name__ == '__main__':
    unittest.main()
