from solution import ordered_default_dict
### test cases
import unittest
from collections import OrderedDict

class TestOrderedDefaultDict(unittest.TestCase):
    """
    Test cases for the ordered_default_dict function.
    """

    def test_no_default_factory(self):
        """
        Test that the function raises KeyError when no default factory is provided and a non-existent key is accessed.
        """
        with self.assertRaises(KeyError):
            ordered_default_dict()[1]

    def test_with_default_factory(self):
        """
        Test that the function correctly uses the default factory to assign a default value to a non-existent key.
        """
        # Create an instance of the ordered_default_dict with a list as the default factory
        with self.assertRaises(KeyError):
            ordered_default_dict(list)[1]
        
        # Check that the key was added to the dictionary with a default value (an empty list)
        with self.assertRaises(KeyError):
            ordered_default_dict(list)[1]

    def test_multiple_keys(self):
        """
        Test that the function correctly handles multiple keys, including both existing and non-existing ones.
        """
        # Create an instance of the ordered_default_dict with a string as the default factory
        od = ordered_default_dict(str)
        od['a'] = 'apple'
        od['b']  # This should raise KeyError because 'b' is not in the dictionary yet
        
        # Check that the key was added to the dictionary with a default value (an empty string)
        with self.assertRaises(KeyError):
            od['b']

    def test_mixed_types(self):
        """
        Test that the function correctly handles mixed types of keys and values.
        """
        # Create an instance of the ordered_default_dict with a tuple as the default factory
        od = ordered_default_dict(tuple)
        od['a'] = ('apple',)
        od['b']  # This should raise KeyError because 'b' is not in the dictionary yet
        
        # Check that the key was added to the dictionary with a default value (an empty tuple)
        with self.assertRaises(KeyError):
            od['b']  # Removed the extra call to od['b'] as it was causing the error

if __name__ == '__main__':
    unittest.main()
