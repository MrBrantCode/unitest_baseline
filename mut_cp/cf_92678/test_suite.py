from solution import print_message
This function uses ANSI escape codes to print colored text. Note: The actual color output may vary based on your terminal settings.

### test cases
import unittest

class TestPrintMessage(unittest.TestCase):
    def test_valid_message(self):
        """
        Test case for a valid message.
        """
        # Arrange
        message = "Hello"
        
        # Act & Assert
        # Since print_message function does not return anything, we will check the printed output manually.
        # We expect the function to print the length of the message and the message three times in different colors.
        print_message(message)
        # Expected output:
        # Message length: 5
        # \033[1m\033[31mHello\033[0m
        # \033[1m\033[32mHello\033[0m
        # \033[1m\033[33mHello\033[0m

    def test_invalid_message_with_numbers(self):
        """
        Test case for an invalid message containing numbers.
        """
        # Arrange
        message = "Hello123"
        
        # Act & Assert
        # Since print_message function does not return anything, we will check the printed output manually.
        # We expect the function to print an error message.
        print_message(message)
        # Expected output:
        # Message can only contain alphabetic characters.

    def test_invalid_message_too_long(self):
        """
        Test case for an invalid message longer than 20 characters.
        """
        # Arrange
        message = "a" * 21
        
        # Act & Assert
        # Since print_message function does not return anything, we will check the printed output manually.
        # We expect the function to print an error message.
        print_message(message)
        # Expected output:
        # Message length cannot exceed 20 characters.

if __name__ == '__main__':
    unittest.main()
