from solution import manipulate_json
### test cases
import unittest
from unittest.mock import patch
import json

class TestManipulateJson(unittest.TestCase):
    def setUp(self):
        # Set up a sample JSON string for testing
        self.sample_json = """
        {
            "name": "Jane Doe",
            "age": 30,
            "email": "janedoe@example.com",
            "address": "123 Elm St",
            "hobbies": ["reading", "traveling"],
            "education": "PhD",
            "friends": [
                {"name": "John Doe", "age": 25, "email": "johndoe@example.com"}
            ]
        }
        """

    def test_valid_input(self):
        # Test with valid input
        result = manipulate_json(self.sample_json)
        expected_result = json.dumps({
            "name": "Jane Doe",
            "age": 30,
            "email": "janedoe@example.com",
            "address": "123 Elm St",
            "hobbies": ["reading", "traveling"],
            "education": "PhD",
            "friends": [
                {"name": "John Doe", "age": 26, "email": "johndoe@example.com"},
                {"name": "Sarah Brown", "age": 26, "email": "sarahbrown@example.com"}
            ]
        }, indent=2)
        self.assertEqual(result, expected_result)

    def test_missing_fields(self):
        # Test with missing fields
        modified_json = self.sample_json.replace('{"name": "John Doe", "age": 25, "email": "johndoe@example.com"}', '')
        result = manipulate_json(modified_json)
        self.assertIn("Missing fields: friends", result)

    def test_invalid_json_format(self):
        # Test with invalid JSON format
        invalid_json = "{'name': 'John Doe', 'age': 25}"
        result = manipulate_json(invalid_json)
        self.assertEqual(result, "Invalid JSON format")

    def test_update_age(self):
        # Test updating the age of "John Doe"
        result = manipulate_json(self.sample_json)
        self.assertEqual(result['friends'][0]['age'], 26)  # Ensure the age of John Doe is updated to 26

    def test_add_new_friend(self):
        # Test adding a new friend
        result = manipulate_json(self.sample_json)
        self.assertIn({"name": "Sarah Brown", "age": 26, "email": "sarahbrown@example.com"}, result['friends'])  # Ensure the new friend is added to the friends list

if __name__ == '__main__':
    unittest.main()
