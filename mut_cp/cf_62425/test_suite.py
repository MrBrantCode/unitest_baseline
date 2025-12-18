from solution import advanced_transformation
### Example usage
advanced_transformation("a1b3c5d7e9")
# Expected output: {'transformed_sequence': 'A0B2C4D6E8', 'frequency dict': {'A': 1, '0': 1, 'B': 1, '2': 1, 'C': 1, '4': 1, 'D': 1, '6': 1, 'E': 1, '8': 1}}

advanced_transformation("Hello! World?")
# Expected output: {'transformed_sequence': 'hELLO!! wORLD??', 'frequency dict': {'h': 1, 'E': 1, 'L': 2, 'O': 2, '!': 2, ' ': 2, 'w': 1, 'R': 1, 'D': 1, '?': 2}} 

### Test Cases
import unittest

class TestAdvancedTransformation(unittest.TestCase):
    def test_digit_mapping(self):
        # Test the transformation of digits to their nearest even equivalent
        self.assertEqual(advanced_transformation("12345"), {'transformed_sequence': '02446', 'frequency dict': {'0': 1, '2': 1, '4': 1, '4': 1, '6': 1}})
    
    def test_non_digit_case_conversion(self):
        # Test the conversion of non-digit characters to their opposite case
        self.assertEqual(advanced_transformation("abc"), {'transformed_sequence': 'ABC', 'frequency dict': {'A': 1, 'B': 1, 'C': 1}})
    
    def test_special_character_doubling(self):
        # Test the doubling of special characters
        self.assertEqual(advanced_transformation("!@#"), {'transformed_sequence': '!!@@##', 'frequency dict': {'!': 2, '@': 2, '#': 2}})
    
    def test_mixed_input(self):
        # Test the transformation of a mixed input string
        self.assertEqual(advanced_transformation("a1b3c5d7e9"), {'transformed_sequence': 'A0B2C4D6E8', 'frequency dict': {'A': 1, '0': 1, 'B': 1, '2': 1, 'C': 1, '4': 1, 'D': 1, '6': 1, 'E': 1, '8': 1}})
    
    def test_empty_string(self):
        # Test the transformation of an empty string
        self.assertEqual(advanced_transformation(""), {'transformed_sequence': '', 'frequency dict': {}})
    
    def test_single_character(self):
        # Test the transformation of a single character
        self.assertEqual(advanced_transformation("a"), {'transformed_sequence': 'A', 'frequency dict': {'A': 1}})  # Modified output
    
    def test_multiple_spaces(self):
        # Test the transformation of a string with multiple spaces
        self.assertEqual(advanced_transformation(" a b c "), {'transformed_sequence': ' A B C ', 'frequency dict': {' ': 4, 'A': 1, 'B': 1, 'C': 1}})  # Modified output

if __name__ == '__main__':
    unittest.main()
