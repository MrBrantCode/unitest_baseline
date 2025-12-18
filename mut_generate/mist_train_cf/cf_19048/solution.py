"""
QUESTION:
Write a function `are_permutations` that determines whether two given strings are permutations of each other, considering case sensitivity, spaces, and punctuation marks. The function should have a time complexity of O(n log n) or better and a space complexity of O(1) or better.
"""

def are_permutations(str1, str2):
    """
    This function determines whether two given strings are permutations of each other, 
    considering case sensitivity, spaces, and punctuation marks.

    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    bool: True if the strings are permutations of each other, False otherwise.
    """
    
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove all spaces and punctuation marks from both strings
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())

    # If the lengths of the two strings are not equal, return False
    if len(str1) != len(str2):
        return False

    # Initialize two arrays, one for the count of each character in the first string and the other for the count of each character in the second string
    count = [0] * 256  # assuming ASCII

    # Iterate through each character in the first string and increment its count
    for char in str1:
        count[ord(char)] += 1

    # Iterate through each character in the second string and decrement its count
    for char in str2:
        count[ord(char)] -= 1

    # If any count is not equal to 0, return False
    for cnt in count:
        if cnt != 0:
            return False

    # If all counts are equal to 0, return True
    return True