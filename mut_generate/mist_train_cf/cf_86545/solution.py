"""
QUESTION:
Write a function named `reverse_string` that takes a string as input, reverses the string, and returns the reversed string. The function must have a time complexity of O(n), where n is the length of the string, and must use constant space complexity, meaning it should not use any additional memory other than the input string.
"""

def entance(s):
    # Convert the string to a list of characters
    chars = list(s)

    # Get the length of the string
    length = len(chars)

    # Initialize two pointers at the beginning and end of the string
    left = 0
    right = length - 1

    # Iterate until the two pointers meet in the middle
    while left < right:
        # Swap the characters at the two pointers
        chars[left], chars[right] = chars[right], chars[left]

        # Move the pointers towards the center
        left += 1
        right -= 1

    # Convert the list of characters back to a string
    reversed_string = ''.join(chars)

    return reversed_string