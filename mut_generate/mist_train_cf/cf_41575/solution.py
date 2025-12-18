"""
QUESTION:
Implement a function `validate_id_number` that takes a string representing a Chinese citizen ID number as input and returns True if the ID number is valid, and False otherwise. The ID number must be a 18-digit string where the last digit is either a digit (0-9) or the letter 'X'. The function should validate the checksum digit using the specified algorithm.
"""

def validate_id_number(id_number):
    if len(id_number) != 18 or not id_number[:-1].isdigit() or id_number[-1] not in '0123456789X':
        return False  

    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checksum_mapping = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

    checksum = sum(int(id_number[i]) * weights[i] for i in range(17)) % 11
    expected_checksum = checksum_mapping[checksum]

    return id_number[-1] == expected_checksum