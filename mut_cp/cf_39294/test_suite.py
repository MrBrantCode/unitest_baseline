from solution import parse_code_snippet
### Test Cases
import unittest

class TestParseCodeSnippet(unittest.TestCase):
    def test_valid_input(self):
        # Test case with valid input
        code = """# @Author: Alice
# @Date  : 2023-04-01
# 100-200"""
        expected_output = ('Alice', '2023-04-01', 100)
        self.assertEqual(parse_code_snippet(code), expected_output)

    def test_invalid_input(self):
        # Test case with invalid input (missing date)
        code = """# @Author: Bob
# @Date  :
# 150-250"""
        self.assertIsNone(parse_code_snippet(code))

    def test_invalid_format(self):
        # Test case with invalid format (missing author)
        code = """# @Date  : 2023-04-01
# @Author: Carol
# 200-300"""
        self.assertIsNone(parse_code_snippet(code))

    def test_no_match(self):
        # Test case where the pattern does not match
        code = """This is a sample code without the required pattern."""
        self.assertIsNone(parse_code_snippet(code))

    def test_extra_information(self):
        # Test case with extra information in the code
        code = """# @Author: Dave
# @Date  : 2023-04-01
# 100-200
# Some extra information here"""
        expected_output = ('Dave', '2023-04-01', 100)
        self.assertEqual(parse_code_snippet(code), expected_output)  # Modified output

    def test_leading_trailing_whitespace(self):
        # Test case with leading and trailing whitespace
        code = """   # @Author: Eve
# @Date  : 2023-04-01
# 50-100   """
        expected_output = ('Eve', '2023-04-01', 50)
        self.assertEqual(parse_code_snippet(code), expected_output)  # Modified output

    def test_multiple_patterns(self):
        # Test case with multiple patterns (only the first one should be matched)
        code = """# @Author: Frank
# @Date  : 2023-04-01
# 100-200
# @Author: Grace
# @Date  : 2023-04-02
# 200-300"""
        expected_output = ('Frank', '2023-04-01', 100)
        self.assertEqual(parse_code_snippet(code), expected_output)  # Modified output

if __name__ == '__main__':
    unittest.main()
