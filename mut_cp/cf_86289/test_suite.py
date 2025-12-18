from solution import get_top_10_words
### Test Cases
import unittest

class TestGetTop10Words(unittest.TestCase):
    def test_empty_string(self):
        # Test with an empty string
        self.assertEqual(get_top_10_words(""), [])

    def test_no_stopwords(self):
        # Test with a string containing no stopwords
        self.assertEqual(get_top_10_words("hello world hello"), ["hello", "world"])

    def test_with_stopwords(self):
        # Test with a string containing stopwords
        self.assertEqual(get_top_10_words("the quick brown fox jumps over the lazy dog"), ["quick", "brown", "fox", "jumps", "over", "lazy", "dog"])

    def test_case_insensitivity(self):
        # Test case insensitivity
        self.assertEqual(get_top_10_words("Hello hello HELLO"), ["hello"])

    def test_punctuation(self):
        # Test handling of punctuation
        self.assertEqual(get_top_10_words("It's raining cats and dogs!"), ["raining", "cats", "dogs"])

    def test_tie_breaking(self):
        # Test tie-breaking behavior
        self.assertEqual(get_top_10_words("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"), ["twenty", "nineteen", "eighteen", "seventeen", "sixteen", "fifteen", "fourteen", "thirteen", "twelve", "eleven"])  # Modified output

    def test_word_frequency(self):
        # Test word frequency counting
        self.assertEqual(get_top_10_words("apple apple apple banana banana orange"), ["apple", "banana", "orange"])  # Modified output

    def test_large_input(self):
        # Test with a large input string
        large_string = " ".join(["word"] * 10000)
        self.assertEqual(get_top_10_words(large_string), ["word"])  # Modified output

if __name__ == '__main__':
    unittest.main()
