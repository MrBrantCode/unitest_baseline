"""
QUESTION:
Write a function `count_ab` that recursively counts the number of occurrences of the substring "ab" in a given string, considering both uppercase and lowercase letters. The input string has a maximum length of 1000 characters, contains only alphabets, and may have overlapping instances of "ab". The function should have a time complexity of O(n), where n is the length of the input string.
"""

def count_ab(text):
    """
    Recursively counts the number of occurrences of the substring "ab" in a given string, 
    considering both uppercase and lowercase letters.

    Args:
        text (str): The input string.

    Returns:
        int: The number of occurrences of "ab" in the input string.
    """

    def count_ab_helper(text, index, count):
        if index >= len(text) - 1:
            return count
        elif text[index:index+2] == "ab":
            count += 1
        return count_ab_helper(text, index + 1, count)

    text = text.lower()
    return count_ab_helper(text, 0, 0)