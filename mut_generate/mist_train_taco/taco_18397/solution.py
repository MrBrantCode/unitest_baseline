"""
QUESTION:
Complete the function that takes a string as an input, and return a list of all the unpaired characters (i.e. they show up an odd number of times in the string), in the order they were encountered as an array. 

In case of multiple appearances to choose from, take the last occurence of the unpaired character.

**Notes:**
* A wide range of characters is used, and some of them may not render properly in your browser.
* Your solution should be linear in terms of string length to pass the last test.


## Examples

```
"Hello World"   -->  ["H", "e", " ", "W", "r", "l", "d"]
"Codewars"      -->  ["C", "o", "d", "e", "w", "a", "r", "s"]
"woowee"        -->  []
"wwoooowweeee"  -->  []
"racecar"       -->  ["e"]
"Mamma"         -->  ["M"]
"Mama"          -->  ["M", "m"]
```
"""

from collections import Counter

def find_unpaired_characters(s: str) -> list:
    # Count the occurrences of each character in the reversed string
    char_count = Counter(reversed(s))
    
    # Filter characters that appear an odd number of times
    unpaired_chars = [char for char in char_count if char_count[char] % 2 != 0]
    
    # Reverse the list to maintain the order of last occurrence
    return unpaired_chars[::-1]