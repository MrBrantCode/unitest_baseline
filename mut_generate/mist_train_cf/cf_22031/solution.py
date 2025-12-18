"""
QUESTION:
Write a function called `reverse_and_remove_duplicates` that takes a string as input, reverses it in place without using any additional data structures, and removes all duplicate characters. The function should have a time complexity of O(n) and a space complexity of O(1). The resulting reversed string should have all duplicate characters removed.
"""

def reverse_and_remove_duplicates(s):
    # Convert the string to a list of characters
    chars = list(s)
    
    # Reverse the list of characters in place
    left = 0
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Remove duplicate characters
    seen = set()
    write_index = 0
    for read_index in range(len(chars)):
        if chars[read_index] not in seen:
            seen.add(chars[read_index])
            chars[write_index] = chars[read_index]
            write_index += 1
    
    # Convert the list of characters back to a string and return it
    return ''.join(chars[:write_index])