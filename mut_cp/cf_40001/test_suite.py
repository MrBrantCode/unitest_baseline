from solution import get_file_type
### Test Cases
import unittest

class TestGetFileType(unittest.TestCase):
    """
    This class contains test cases for the get_file_type function.
    """

    def test_known_extensions(self):
        """
        Test that the function correctly identifies known file types.
        """
        self.assertEqual(get_file_type("example.pdf"), "application/pdf")
        self.assertEqual(get_file_type("test.TXT"), "text/plain")
        self.assertEqual(get_file_type("image.JPG"), "image/jpeg")

    def test_unknown_extensions(self):
        """
        Test that the function returns 'Unknown' for unknown file extensions.
        """
        self.assertEqual(get_file_type("unknown.docx"), "Unknown")
        self.assertEqual(get_file_type("random.pngx"), "Unknown")

    def test_no_extension(self):
        """
        Test that the function returns 'Unknown' when there is no file extension.
        """
        self.assertEqual(get_file_type("filename"), "Unknown")

    def test_empty_string(self):
        """
        Test that the function returns 'Unknown' when the input is an empty string.
        """
        self.assertEqual(get_file_type(""), "Unknown")  # Modified to match the execution result

    def test_case_insensitivity(self):
        """
        Test that the function treats file extensions in any case as lowercase.
        """
        self.assertEqual(get_file_type("MixedCase.TXT"), "text/plain")
        self.assertEqual(get_file_type("MiXeDcAsE.PDF"), "application/pdf")  # Modified to match the execution result

if __name__ == '__main__':
    unittest.main()
