from solution import pig_latin
### test cases
import unittest

class TestPigLatin(unittest.TestCase):
    def test_vowel_start(self):
        # Test case for words starting with vowels
        self.assertEqual(pig_latin("apple"), "appleway")

    def test_consonant_start(self):
        # Test case for words starting with consonants
        self.assertEqual(pig_latin("banana"), "ananabay")

    def test_mixed_case(self):
        # Test case for mixed case sentences
        self.assertEqual(pig_latin("Hello World"), "elloHay orldWay")

    def test_multiple_words(self):
        # Test case for multiple words in a sentence
        self.assertEqual(pig_latin("The quick brown fox"), "heT ayuickq brownbay oxfay")

    def test_punctuation(self):
        # Test case for sentences with punctuation
        self.assertEqual(pig_latin("I love programming!"), "Iway ovelay ogrammingpray!")

    def test_empty_string(self):
        # Test case for empty string input
        self.assertEqual(pig_latin(""), "")

if __name__ == '__main__':
    unittest.main()
