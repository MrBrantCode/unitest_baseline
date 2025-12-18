"""
QUESTION:
Implement a function `reverse_string` that takes a string as input and returns the reversed string. The function should not use any additional data structures, loops, or recursion, but this requirement is actually impossible because at least a loop is necessary to iterate through the string. Therefore, the loop is used here but other requirements such as not using any additional data structures, built-in string manipulation functions, or methods are still kept. The function should have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(string):
    # Convert string to a list of characters
    string_arr = list(string)
    
    # Define two pointers
    start = 0
    end = len(string_arr) - 1
    
    # Swap characters until the pointers meet or cross each other
    while start < end:
        # Use XOR swap to swap characters in place
        string_arr[start] = chr(ord(string_arr[start]) ^ ord(string_arr[end]))
        string_arr[end] = chr(ord(string_arr[start]) ^ ord(string_arr[end]))
        string_arr[start] = chr(ord(string_arr[start]) ^ ord(string_arr[end]))
        
        # Increment the first pointer and decrement the second pointer
        start += 1
        end -= 1
    
    # Convert the list back into a string
    reversed_string = ''.join(string_arr)
    
    return reversed_string