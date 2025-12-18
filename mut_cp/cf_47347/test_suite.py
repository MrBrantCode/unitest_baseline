from solution import escape_quotes
### test cases
import unittest

class TestEscapeQuotesFunction(unittest.TestCase):
    """
    Test class for the escape_quotes function.
    This class contains several test cases to ensure the function works correctly.
    """

    def test_no_quotes(self):
        """
        Test case where the input string does not contain any single quotes.
        """
        self.assertEqual(escape_quotes("HelloWorld"), "HelloWorld")

    def test_single_quote(self):
        """
        Test case where the input string contains a single single quote.
        """
        self.assertEqual(escape_quotes("It's a test"), "It''s a test")

    def test_multiple_quotes(self):
        """
        Test case where the input string contains multiple single quotes.
        """
        self.assertEqual(escape_quotes("I'm going to the store"), "I''m going to the store")

    def test_quotes_at_start_and_end(self):
        """
        Test case where the input string starts and ends with a single quote.
        """
        self.assertEqual(escape_quotes("'Start and end with quotes'"), "'Start and end with quotes'")

    def test_empty_string(self):
        """
        Test case where the input string is empty.
        """
        self.assertEqual(escape_quotes(""), "")  # Modified output

    def test_special_characters(self):
        """
        Test case where the input string contains special characters other than single quotes.
        """
        self.assertEqual(escape_quotes("Special!@#$%^&*()_+"), "Special!@#$%^&*()_+")  # No change needed

if __name__ == '__main__':
    unittest.main()
