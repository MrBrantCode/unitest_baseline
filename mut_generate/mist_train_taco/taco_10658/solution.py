"""
QUESTION:
Given a string str and another string patt. Find the minimum index of the character in str that is also present in patt.
Example 1:
Input:
str = geeksforgeeks
patt = set
Output: 1
Explanation: e is the character which is
present in given str "geeksforgeeks"
and is also presen in patt "set". Minimum
index of e is 1. 
Example 2:
Input:
str = adcffaet
patt = onkl
Output: -1
Explanation: There are none of the
characters which is common in patt
and str.
Your Task:
You only need to complete the function minIndexChar() that returns the index of answer in str or returns -1 in case no character of patt is present in str.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Constraints:
1 ≤ |str|,|patt| ≤ 10^{5 }
'a' <= str_{i}, patt_{i} <= 'z'
"""

def find_min_index_of_common_char(str_input: str, patt: str) -> int:
    char_index_map = {}
    for index, char in enumerate(str_input):
        if char not in char_index_map:
            char_index_map[char] = index
    
    min_index = float('inf')
    for char in patt:
        if char in char_index_map:
            min_index = min(min_index, char_index_map[char])
    
    return min_index if min_index != float('inf') else -1