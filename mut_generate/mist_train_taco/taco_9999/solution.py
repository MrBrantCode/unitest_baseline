"""
QUESTION:
In this Kata, we are going to see how a Hash (or Map or dict) can be used to keep track of characters in a string. 

Consider two strings `"aabcdefg"` and `"fbd"`. How many characters do we have to remove from the first string to get the second string?  Although not the only way to solve this, we could create a Hash of counts for each string and see which character counts are different. That should get us close to the answer. I will leave the rest to you. 

For this example, `solve("aabcdefg","fbd") = 5`. Also, `solve("xyz","yxxz") = 0`, because we cannot get second string from the first since the second string is longer.

More examples in the test cases.

Good luck!
"""

from collections import Counter

def characters_to_remove(first_string: str, second_string: str) -> int:
    # Count the characters in both strings
    count_first = Counter(first_string)
    count_second = Counter(second_string)
    
    # Check if we can obtain the second string from the first string
    if count_second - count_first:
        return 0
    
    # Calculate the number of characters to remove
    return len(first_string) - len(second_string)