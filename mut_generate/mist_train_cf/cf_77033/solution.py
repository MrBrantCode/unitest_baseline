"""
QUESTION:
Create a function `valid_scholar_info` that takes a dictionary of scholar data as input, where each key is a scholar ID and each value is another dictionary containing the scholar's information (name and age). The function should validate the scholar's name and age against the following rules: 
- The name should only contain alphabets and spaces.
- The age should be an integer between 18 and 99.
The function should return a dictionary with the same scholar IDs as keys and boolean values indicating whether the corresponding scholar's information is valid. 
The function should be able to handle large amounts of data efficiently.
"""

import re

def valid_scholar_info(scholar_data):
    """Checks if scholar info (name and age) is valid"""
    def valid_name(name):
        """Checks if the given name is valid"""
        # The regular expression "^[a-zA-Z ]*$" checks if name only contains alphabets & spaces
        return bool(re.match("^[a-zA-Z ]*$", name))

    def valid_age(age):
        """Checks if the given age is valid"""
        return 18 <= age <= 99

    return {scholar_id: valid_name(info["name"]) and valid_age(info["age"]) for scholar_id, info in scholar_data.items()}