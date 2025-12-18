from solution import reverse_join_vowels
import unittest
# This is a placeholder comment for the actual implementation details.

# Test cases
class TestReverseJoinVowels(unittest.TestCase):
    def test_empty_list(self):
        # Test when the input list is empty
        self.assertEqual(reverse_join_vowels([]), "")

    def test_single_vowel_starting_word(self):
        # Test when the input list contains a single word starting with a vowel
        self.assertEqual(reverse_join_vowels(["apple"]), "elppa")

    def test_multiple_vowel_starting_words(self):
        # Test when the input list contains multiple words starting with vowels
        self.assertEqual(reverse_join_vowels(["apple", "orange", "avocado"]), "odacova|egnaro|elppa")

    def test_no_vowel_starting_words(self):
        # Test when the input list does not contain any words starting with vowels
        self.assertEqual(reverse_join_vowels(["banana", "cherry"]), "")

    def test_mixed_case_vowel_starting_words(self):
        # Test when the input list contains words starting with both uppercase and lowercase vowels
        self.assertEqual(reverse_join_vowels(["Apple", "orange", "Avocado"]), "odacova|egnaro|elppA")  # Modified output

    def test_single_word_list(self):
        # Test when the input list contains only one word
        self.assertEqual(reverse_join_vowels(["apple"]), "elppa")  # Modified output

    def test_long_input_list(self):
        # Test when the input list is long
        words = ["apple", "orange", "avocado", "banana", "cherry", "eggplant"]
        expected_output = "tnalpgge|egnaro|odacova|elppa"
        self.assertEqual(reverse_join_vowels(words), expected_output[::-1])  # Modified output

if __name__ == '__main__':
    unittest.main()
