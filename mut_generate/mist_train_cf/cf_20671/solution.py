"""
QUESTION:
Write a recursive function `count_substring_ab` that takes a string and returns the number of times the substring "ab" appears in the string, considering both uppercase and lowercase letters. The input string is restricted to a maximum length of 1000 characters and only contains alphabets. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def count_substring_ab(string):
    """
    Counts the number of occurrences of the substring "ab" in the given string, 
    considering both uppercase and lowercase letters.

    Args:
        string (str): The input string.

    Returns:
        int: The number of occurrences of the substring "ab".
    """
    def recursive_count(string, index, count):
        if index >= len(string) - 1:  # Check if there are at least two characters left
            return count
        
        if string[index:index+2].lower() == "ab":
            count += 1

        return recursive_count(string, index + 1, count)

    return recursive_count(string, 0, 0)