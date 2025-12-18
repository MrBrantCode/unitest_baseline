"""
QUESTION:
Create a function unique_sorted_string that takes a list of strings as input and returns a string with all unique characters from the input strings in lexicographic order. The function must handle edge cases such as empty input list or empty strings in the input list. The function should achieve this in O(NlogN) time complexity and O(N) space complexity, where N is the total number of characters in all the strings combined, without using any built-in sorting or deduplication functions or libraries, additional data structures like sets or dictionaries, or additional libraries or modules.
"""

def unique_sorted_string(strings):
    if not strings: # handle empty input list
        return ''
    
    string = ''.join(strings) # concatenate all strings
    
    if not string: # handle empty strings in the input list
        return ''
    
    string = sorted(string) # sort the characters in lexicographic order
    
    unique_string = ''
    prev_char = ''
    
    for char in string:
        if char != prev_char:
            unique_string += char
            prev_char = char
    
    return unique_string