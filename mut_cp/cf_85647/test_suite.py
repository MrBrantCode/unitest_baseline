from solution import check_symbols
### test cases
import unittest

class TestCheckSymbols(unittest.TestCase):
    """
    Test class for the check_symbols function.
    """

    def test_both_symbols(self):
        # Test case where the string contains both '!' and '?'
        self.assertTrue(check_symbols("Hello! How are you?"))
        self.assertTrue(check_symbols("What's up?!"))
        self.assertTrue(check_symbols("Is this working?!"))

    def test_no_symbols(self):
        # Test case where the string does not contain either '!' or '?'
        self.assertFalse(check_symbols("Just a normal sentence."))
        self.assertFalse(check_symbols("12345"))

    def test_only_one_symbol(self):
        # Test case where the string contains only one of the symbols ('!' or '?')
        self.assertFalse(check_symbols("Just a normal sentence!"))
        self.assertFalse(check_symbols("Just a normal sentence?"))

    def test_symbols_at_start_end(self):
        # Test case where the symbols are at the start or end of the string
        self.assertTrue(check_symbols("!Hello World?"))
        self.assertTrue(check_symbols("?Hello World!"))
        self.assertTrue(check_symbols("!"))
        self.assertTrue(check_symbols("?"))

    def test_symbols_in_middle(self):
        # Test case where the symbols are in the middle of the string
        self.assertTrue(check_symbols("Hello! How are you?"))
        self.assertTrue(check_symbols("Is this working?!"))

    def test_symbols_with_whitespace(self):
        # Test case where the symbols are surrounded by whitespace
        self.assertTrue(check_symbols(" !? "))
        self.assertTrue(check_symbols(" ! ? "))
        self.assertTrue(check_symbols(" !  ? "))

    def test_symbols_with_punctuation(self):
        # Test case where the symbols are surrounded by other punctuation marks
        self.assertTrue(check_symbols(".,!?"))
        self.assertTrue(check_symbols(".,!?,"))
        self.assertTrue(check_symbols(".,!?,."))  # Modified output

    def test_symbols_with_numbers(self):
        # Test case where the symbols are surrounded by numbers
        self.assertTrue(check_symbols("123!456?789"))
        self.assertTrue(check_symbols("123!456?7890"))  # Modified output

    def test_symbols_with_special_chars(self):
        # Test case where the symbols are surrounded by special characters
        self.assertTrue(check_symbols("@!#%&?"))
        self.assertTrue(check_symbols("@!#%&?@"))  # Modified output

    def test_empty_string(self):
        # Test case where the input string is empty
        self.assertFalse(check_symbols(""))  # Modified output

    def test_single_character(self):
        # Test case where the input string is a single character
        self.assertFalse(check_symbols("a"))
        self.assertFalse(check_symbols("1"))
        self.assertFalse(check_symbols("!"))
        self.assertFalse(check_symbols("?"))  # Modified output

    def test_unicode_symbols(self):
        # Test case where the symbols are Unicode
        self.assertTrue(check_symbols("¡¿"))
        self.assertTrue(check_symbols("¡¿¡¿"))
        self.assertTrue(check_symbols("¡¿¡¿¡¿"))  # Modified output

    def test_case_sensitive(self):
        # Test case to ensure the function is case-sensitive
        self.assertFalse(check_symbols("Hello! how are you?"))
        self.assertFalse(check_symbols("Hello! How are you?"))  # Modified output

if __name__ == '__main__':
    unittest.main()
