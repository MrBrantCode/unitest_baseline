from solution import deep_copy
### test cases
import unittest

class TestDeepCopyFunction(unittest.TestCase):
    def test_deep_copy_string(self):
        # Test case for string
        original_str = "Hello"
        copied_str = deep_copy(original_str)
        self.assertEqual(original_str, copied_str)

    def test_deep_copy_int(self):
        # Test case for integer
        original_int = 123
        copied_int = deep_copy(original_int)
        self.assertEqual(original_int, copied_int)

    def test_deep_copy_float(self):
        # Test case for float
        original_float = 123.45
        copied_float = deep_copy(original_float)
        self.assertEqual(original_float, copied_float)

    def test_deep_copy_boolean(self):
        # Test case for boolean
        original_bool = True
        copied_bool = deep_copy(original_bool)
        self.assertEqual(original_bool, copied_bool)

    def test_deep_copy_none(self):
        # Test case for None
        original_none = None
        copied_none = deep_copy(original_none)
        self.assertIsNone(copied_none)

    def test_deep_copy_dict(self):
        # Test case for dictionary
        original_dict = {'a': 1, 'b': 2}
        copied_dict = deep_copy(original_dict)
        self.assertIsNot(original_dict, copied_dict)
        self.assertEqual(original_dict, copied_dict)

    def test_deep_copy_list(self):
        # Test case for list
        original_list = [1, 2, 3]
        copied_list = deep_copy(original_list)
        self.assertIsNot(original_list, copied_list)
        self.assertEqual(original_list, copied_list)

    def test_deep_copy_nested_dict(self):
        # Test case for nested dictionary
        original_nested_dict = {'a': {'b': 1}}
        copied_nested_dict = deep_copy(original_nested_dict)
        self.assertIsNot(original_nested_dict, copied_nested_dict)
        self.assertEqual(original_nested_dict, copied_nested_dict)

    def test_deep_copy_nested_list(self):
        # Test case for nested list
        original_nested_list = [1, [2, 3]]
        copied_nested_list = deep_copy(original_nested_list)
        self.assertIsNot(original_nested_list, copied_nested_list)
        self.assertEqual(original_nested_list, copied_nested_list)

    def test_deep_copy_mixed_types(self):
        # Test case for mixed types
        original_mixed = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
        copied_mixed = deep_copy(original_mixed)
        self.assertIsNot(original_mixed, copied_mixed)
        self.assertEqual(original_mixed, copied_mixed)

if __name__ == '__main__':
    unittest.main()
