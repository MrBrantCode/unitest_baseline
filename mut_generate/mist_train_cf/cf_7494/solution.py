"""
QUESTION:
Write a function called `reverse_string` that takes a string as input, reverses the string in place, removes all duplicate characters, and returns the resulting string. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def entance(string):
    # Convert the string to a list of characters
    char_list = list(string)
    
    # Reverse the list in place using two pointers
    left = 0
    right = len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    # Remove duplicate characters using two pointers
    slow = 0
    fast = 1
    while fast < len(char_list):
        if char_list[fast] != char_list[slow]:
            slow += 1
            char_list[slow] = char_list[fast]
        fast += 1
    
    # Convert the list back to a string
    result = ''.join(char_list[:slow+1])
    
    return result