from solution import organize_list
### test cases
import unittest

class TestOrganizeList(unittest.TestCase):
    """
    This class contains unit tests for the organize_list function.
    """

    def setUp(self):
        """
        Set up the initial data for the tests.
        """
        self.data = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 30}
        ]
        self.empty_data = []

    def test_sort_by_name(self):
        """
        Test sorting by 'name' key.
        """
        sorted_data = organize_list(self.data, 'name')
        expected_output = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 30}
        ]
        self.assertEqual(sorted_data, expected_output)

    def test_sort_by_age(self):
        """
        Test sorting by 'age' key.
        """
        sorted_data = organize_list(self.data, 'age')
        expected_output = [
            {'name': 'Bob', 'age': 22},
            {'name': 'Alice', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ]
        self.assertEqual(sorted_data, expected_output)

    def test_sort_empty_list(self):
        """
        Test sorting an empty list.
        """
        sorted_data = organize_list(self.empty_data, 'name')
        expected_output = []
        self.assertEqual(sorted_data, expected_output)  # No change needed here

    def test_sort_with_duplicate_values(self):
        """
        Test sorting with duplicate values for the specified key.
        """
        data_with_duplicates = [
            {'name': 'Alice', 'age': 25},
            {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 30},
            {'name': 'David', 'age': 22}
        ]
        sorted_data = organize_list(data_with_duplicates, 'age')
        expected_output = [
            {'name': 'Bob', 'age': 22},
            {'name': 'David', 'age': 22},
            {'name': 'Alice', 'age': 25},
            {'name': 'Charlie', 'age': 30}
        ]
        self.assertEqual(sorted_data, expected_output)  # No change needed here

    def test_sort_nonexistent_key(self):
        """
        Test sorting with a key that does not exist in the dictionaries.
        This test will fail because the function does not handle non-existent keys gracefully.
        """
        with self.assertRaises(KeyError):
            organize_list(self.data, 'nonexistent_key')  # No change needed here

if __name__ == '__main__':
    unittest.main()
