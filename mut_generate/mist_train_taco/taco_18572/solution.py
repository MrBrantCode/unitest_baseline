"""
QUESTION:
You'll be given a list of two strings, and each will contain exactly one colon (`":"`) in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.


## Examples
```
["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]
```
"""

def swap_after_colon(strings):
    # Split the first string into head and tail
    head0, tail0 = strings[0].split(':')
    
    # Split the second string into head and tail
    head1, tail1 = strings[1].split(':')
    
    # Return the new list with swapped tails
    return [head0 + ':' + tail1, head1 + ':' + tail0]