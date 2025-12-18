from solution import reversePrefix
### test cases
import unittest

class TestReversePrefix(unittest.TestCase):
    def test_reverse_prefix_with_ch_in_word(self):
        # Test case where 'ch' is present in the word.
        self.assertEqual(reversePrefix("hello", "l"), "lehlo")
        
    def test_reverse_prefix_with_ch_not_in_word(self):
        # Test case where 'ch' is not present in the word.
        self.assertEqual(reversePrefix("world", "x"), "world")
        
    def test_reverse_prefix_with_ch_at_start(self):
        # Test case where 'ch' is at the start of the word.
        self.assertEqual(reversePrefix("apple", "a"), "apple")
        
    def test_reverse_prefix_with_ch_at_end(self):
        # Test case where 'ch' is at the end of the word.
        self.assertEqual(reversePrefix("banana", "a"), "anana")
        
    def test_reverse_prefix_with_single_character_word(self):
        # Test case with a single character word.
        self.assertEqual(reversePrefix("a", "a"), "a")
        
    def test_reverse_prefix_with_empty_string(self):
        # Test case with an empty string.
        self.assertEqual(reversePrefix("", "a"), "")
        
    def test_reverse_prefix_with_ch_repeated(self):
        # Test case where 'ch' is repeated in the word.
        self.assertEqual(reversePrefix("mississippi", "i"), "misssippi")  # Modified output

if __name__ == '__main__':
    unittest.main()
