from solution import sort_dictionary_by_meanings
### test cases
import unittest

class TestSortDictionaryByMeanings(unittest.TestCase):
    """
    Test cases for the function sort_dictionary_by_meanings.
    """

    def test_sort_by_number_of_meanings(self):
        # Test case with words having different numbers of meanings
        test_dict = {'apple': ['fruit', 'company'], 'banana': ['fruit'], 'carrot': ['vegetable']}
        expected_output = ['banana', 'carrot', 'apple']
        self.assertEqual(sort_dictionary_by_meanings(test_dict), expected_output)

    def test_sort_with_same_number_of_meanings(self):
        # Test case with words having the same number of meanings
        test_dict = {'dog': ['pet', 'animal'], 'cat': ['pet', 'animal'], 'fish': ['pet']}
        expected_output = ['fish', 'dog', 'cat']  # Order of 'dog' and 'cat' is not specified
        self.assertEqual(sort_dictionary_by_meanings(test_dict), expected_output)

    def test_sort_empty_dictionary(self):
        # Test case with an empty dictionary
        test_dict = {}
        expected_output = []
        self.assertEqual(sort_dictionary_by_meanings(test_dict), expected_output)

    def test_sort_single_word(self):
        # Test case with a single word in the dictionary
        test_dict = {'single': ['meaning']}
        expected_output = ['single']
        self.assertEqual(sort_dictionary_by_meanings(test_dict), expected_output)  # Modified output

if __name__ == '__main__':
    unittest.main()
