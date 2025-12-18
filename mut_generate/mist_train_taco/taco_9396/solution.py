"""
QUESTION:
Seven is a hungry number and its favourite food is number 9. Whenever it spots 9
through the hoops of 8, it eats it! Well, not anymore, because you are 
going to help the 9 by locating that particular sequence (7,8,9) in an array of digits
and tell 7 to come after 9 instead. Seven "ate" nine, no more!
(If 9 is not in danger, just return the same array)
"""

import re

def relocate_hungry_seven(arr):
    # Convert the list of integers to a string for easier manipulation
    s = ''.join(map(str, arr))
    
    # Use regular expressions to find and replace the sequence '7+89' with '897+'
    while True:
        new_s = re.sub('(7+)(89)', '\\2\\1', s)
        if new_s == s:
            break
        s = new_s
    
    # Convert the modified string back to a list of integers
    return list(map(int, s))