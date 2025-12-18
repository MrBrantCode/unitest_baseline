from solution import rgb_to_hex
#unittest

import unittest

class TestRgbToHex(unittest.TestCase):
    def test_integer_input(self):
        # Test case for integer input
        self.assertEqual(rgb_to_hex(255), "#ffffff")
        self.assertEqual(rgb_to_hex(0), "#000000")
        self.assertEqual(rgb_to_hex(-1), "Invalid RGB value")
        self.assertEqual(rgb_to_hex(256), "Invalid RGB value")

    def test_float_input(self):
        # Test case for float input
        self.assertEqual(rgb_to_hex(255.0), "#ffffff")
        self.assertEqual(rgb_to_hex(0.5), "#000000")
        self.assertEqual(rgb_to_hex(-0.5), "Invalid RGB value")
        self.assertEqual(rgb_to_hex(256.0), "Invalid RGB value")

    def test_string_input(self):
        # Test case for string input
        self.assertEqual(rgb_to_hex("255"), "#ffffff")
        self.assertEqual(rgb_to_hex("0"), "#000000")
        self.assertEqual(rgb_to_hex("invalid"), "Invalid input type")

    def test_tuple_input(self):
        # Test case for tuple input
        self.assertEqual(rgb_to_hex((255, 0, 0)), "#ff0000")
        self.assertEqual(rgb_to_hex((0, 0, 0)), "#000000")
        self.assertEqual(rgb_to_hex((255, -1, 0)), "Invalid RGB value")
        self.assertEqual(rgb_to_hex((255, 256, 0)), "Invalid RGB value")
        self.assertEqual(rgb_to_hex((255, 0, "0")), "Invalid input type")
        self.assertEqual(rgb_to_hex((255, 0, (0,))), "Invalid input type")

    def test_invalid_input_types(self):
        # Test case for invalid input types
        self.assertEqual(rgb_to_hex([255, 0, 0]), "Invalid input type")
        self.assertEqual(rgb_to_hex(None), "Invalid input type")
        self.assertEqual(rgb_to_hex(True), "Invalid input type") # Modified here

if __name__ == '__main__':
    unittest.main()
