from solution import filter_keywords
### test cases
import unittest

class TestFilterKeywords(unittest.TestCase):
    def test_no_keywords(self):
        # Test when there are no keywords to remove.
        self.assertEqual(filter_keywords("Hello World", []), "Hello World")

    def test_single_keyword(self):
        # Test when there is one keyword to remove.
        self.assertEqual(filter_keywords("Hello World", ["World"]), "Hello ")

    def test_multiple_keywords(self):
        # Test when there are multiple keywords to remove.
        self.assertEqual(filter_keywords("Hello World", ["Hello", "World"]), " ")

    def test_keywords_with_punctuation(self):
        # Test when keywords contain punctuation marks.
        self.assertEqual(filter_keywords("Hello, World!", ["Hello,", "World!"]), ", !")

    def test_keywords_with_capitalization(self):
        # Test when keywords have different capitalizations.
        self.assertEqual(filter_keywords("Hello World", ["hello", "WORLD"]), "Hello World")

    def test_keywords_in_middle_of_words(self):
        # Test when keywords appear in the middle of words.
        self.assertEqual(filter_keywords("HellooWorld", ["Hello", "World"]), "o")

    def test_keywords_not_in_text(self):
        # Test when keywords do not appear in the text.
        self.assertEqual(filter_keywords("Hello World", ["Goodbye", "Universe"]), "Hello World")

    def test_empty_text(self):
        # Test when the input text is empty.
        self.assertEqual(filter_keywords("", ["Hello", "World"]), "")

    def test_empty_keywords_list(self):
        # Test when the list of keywords is empty.
        self.assertEqual(filter_keywords("Hello World", []), "Hello World")  # Modified output

    def test_keywords_longer_than_text(self):
        # Test when keywords are longer than the text.
        self.assertEqual(filter_keywords("Hi", ["Hello", "World"]), "Hi")  # Modified output

    def test_keywords_same_as_text(self):
        # Test when keywords are the same as the text.
        self.assertEqual(filter_keywords("Hello", ["Hello"]), "")  # Modified output

    def test_keywords_with_special_characters(self):
        # Test when keywords contain special characters.
        self.assertEqual(filter_keywords("Hello World", ["Hello$", "World!"]), "Hello World")  # Modified output

if __name__ == '__main__':
    unittest.main()
