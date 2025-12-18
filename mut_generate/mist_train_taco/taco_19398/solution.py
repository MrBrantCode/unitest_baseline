"""
QUESTION:
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).
 
Example 1:
Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".

Example 2:
Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".

 
Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.
"""

from collections import defaultdict, deque

def count_distinct_echo_substrings(text: str) -> int:
    if all((x == text[0] for x in text)):
        return len(text) // 2
    
    res = set()
    character_locations = defaultdict(lambda: deque())
    
    for i, c in enumerate(text):
        for j in character_locations[c]:
            if i + (i - j) > len(text):
                break
            if text.startswith(text[i:i + i - j], j):
                res.add(text[j:i + i - j])
        character_locations[c].appendleft(i)
    
    return len(res)