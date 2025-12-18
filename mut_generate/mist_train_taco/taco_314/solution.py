"""
QUESTION:
## Task
Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.

### Example:

```
Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
```

Good luck!
"""

def reverse_strings_and_order(strings):
    # Join all strings into one large string and reverse it
    reversed_joined_string = ''.join(strings)[::-1]
    
    # Create a list of reversed strings by slicing the reversed_joined_string
    reversed_strings = []
    start_index = 0
    for string in strings:
        end_index = start_index + len(string)
        reversed_strings.append(reversed_joined_string[start_index:end_index])
        start_index = end_index
    
    return reversed_strings