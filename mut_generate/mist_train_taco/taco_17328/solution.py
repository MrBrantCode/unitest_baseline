"""
QUESTION:
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.



Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.



Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

import collections

def sort_string_by_frequency(s: str) -> str:
    # Count the frequency of each character in the string
    counter = collections.Counter(s)
    
    # Sort the characters by their frequency in descending order
    sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    
    # Construct the result string by repeating each character by its frequency
    result = ''.join(char * freq for char, freq in sorted_items)
    
    return result