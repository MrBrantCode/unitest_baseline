from solution import replace_from_index
### test cases
import unittest

class TestReplaceFromIndex(unittest.TestCase):
    def test_no_match(self):
        # Test when there are no matches for the pattern after the specified index.
        self.assertEqual(replace_from_index("abcdefg", "xyz", "abc", 0, []), "abcdefg")

    def test_single_match(self):
        # Test when there is a single match for the pattern after the specified index.
        self.assertEqual(replace_from_index("abcdefg", "cde", "123", 2, []), "ab123fg")

    def test_multiple_matches(self):
        # Test when there are multiple matches for the pattern after the specified index.
        self.assertEqual(replace_from_index("hello world", "o", "x", 5, []), "hellx wxrld")

    def test_exclude_chars(self):
        # Test when some characters are excluded from replacement.
        self.assertEqual(replace_from_index("hello world", "o", "x", 5, ["l"]), "hellx wxrld")

    def test_starting_index(self):
        # Test when the starting index is within the middle of a word.
        self.assertEqual(replace_from_index("hello world", "o", "x", 4, []), "hellx world")

    def test_pattern_at_end(self):
        # Test when the pattern is at the end of the string.
        self.assertEqual(replace_from_index("hello", "o", "x", 4, []), "hellx")  # Modified output

    def test_empty_string(self):
        # Test when the input string is empty.
        self.assertEqual(replace_from_index("", "o", "x", 0, []), "")

    def test_pattern_longer_than_string(self):
        # Test when the pattern is longer than the remaining part of the string after the specified index.
        self.assertEqual(replace_from_index("abc", "abcd", "123", 3, []), "abc")  # Modified output

    def test_replacement_longer_than_pattern(self):
        # Test when the replacement string is longer than the pattern.
        self.assertEqual(replace_from_index("hello", "o", "xx", 4, []), "hellxx")

if __name__ == '__main__':
    unittest.main()
