from solution import convert_octal
### test cases
import unittest

class TestConvertOctal(unittest.TestCase):
    """
    Test class for the convert_octal function.
    """

    def test_valid_octal(self):
        """
        Test case for a valid octal number.
        """
        # Arrange
        octal = "12"
        expected_output = (10, '1010', 'a')
        
        # Act
        result = convert_octal(octal)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_zero_octal(self):
        """
        Test case for an octal number that is zero.
        """
        # Arrange
        octal = "0"
        expected_output = (0, '0', '0')
        
        # Act
        result = convert_octal(octal)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_large_octal(self):
        """
        Test case for a large octal number.
        """
        # Arrange
        octal = "7777777777"
        expected_output = (511, '11111111111111111111111111111111', '1ff')
        
        # Act
        result = convert_octal(octal)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_invalid_octal(self):
        """
        Test case for an invalid octal number.
        """
        # Arrange
        octal = "8"
        # Act & Assert
        with self.assertRaises(ValueError):
            convert_octal(octal)  # This will raise ValueError if the input is invalid

    def test_empty_string(self):
        """
        Test case for an empty string input.
        """
        # Arrange
        octal = ""
        # Act & Assert
        with self.assertRaises(ValueError):
            convert_octal(octal)  # This will raise ValueError if the input is empty

    def test_whitespace_input(self):
        """
        Test case for whitespace input.
        """
        # Arrange
        octal = "   "
        # Act & Assert
        with self.assertRaises(ValueError):
            convert_octal(octal)  # This will raise ValueError if the input contains whitespace

if __name__ == '__main__':
    unittest.main()
