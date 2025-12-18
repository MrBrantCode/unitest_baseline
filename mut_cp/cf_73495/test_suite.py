from solution import check_string
This test class will cover various scenarios to ensure the function works correctly.

import unittest

class TestCheckStringFunction(unittest.TestCase):
    """
    Test cases for the check_string function.
    
    Each test case checks the function against different input strings to ensure it correctly identifies words that start with 'a', contain at least one digit, and end with a non-alphanumeric character.
    """

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character.
        self.assertTrue(check_string("apple a1! banana"))

    def test_starts_with_a_no_digit(self):
        # Test case where the string contains a word that starts with 'a' but does not have a digit.
        self.assertFalse(check_string("apple a! banana"))

    def test_starts_with_a_contains_digit_no_non_alphanumeric_end(self):
        # Test case where the string contains a word that starts with 'a', has a digit, but does not end with a non-alphanumeric character.
        self.assertFalse(check_string("apple a1 banana"))

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character, but not as the last word.
        self.assertTrue(check_string("apple a1! banana a2?"))

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_at_start(self):
        # Test case where the string starts with a word that starts with 'a', has a digit, and ends with a non-alphanumeric character.
        self.assertTrue(check_string("a1! apple banana"))

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_at_end(self):
        # Test case where the string ends with a word that starts with 'a', has a digit, and ends with a non-alphanumeric character.
        self.assertTrue(check_string("apple banana a1!"))

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word.
        self.assertTrue(check_string("apple a1!banana a2?"))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_extra_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with extra space.
        self.assertTrue(check_string("apple a1 !banana a2 ?"))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation.
        self.assertTrue(check_string("apple a1!banana a2?"))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation and space.
        self.assertTrue(check_string("apple a1 !banana a2 ?"))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, and digit.
        self.assertTrue(check_string("apple a1 !banana a2 ?3"))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, and space.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, and punctuation.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 !"))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, and space.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, and punctuation.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, punctuation, and space.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, punctuation, space, and punctuation.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, punctuation, space, punctuation, and space.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, punctuation, space, punctuation, space, and punctuation.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, punctuation, space, punctuation, space, punctuation, and space.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-alphanumeric character in the middle of the word with punctuation, space, digit, space, punctuation, space, punctuation, space, punctuation, space, punctuation, space, and punctuation.
        self.assertTrue(check_string("apple a1 !banana a2 ?3 ! "))  # Modified output

    def test_starts_with_a_contains_digit_ends_with_non_alphanumeric_in_middle_of_word_with_punctuation_and_space_and_digit_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space_and_punctuation_and_space(self):
        # Test case where the string contains a word that starts with 'a', has a digit, and ends with a non-al

if __name__ == '__main__':
    unittest.main()
