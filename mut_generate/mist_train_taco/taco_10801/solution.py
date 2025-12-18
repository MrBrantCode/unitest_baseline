"""
QUESTION:
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
 
Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

Example 4:
Input: n = 2, k = 7
Output: ""

Example 5:
Input: n = 10, k = 100
Output: "abacbabacb"

 
Constraints:

1 <= n <= 10
1 <= k <= 100
"""

def find_kth_happy_string(n: int, k: int) -> str:
    def index_to_str(index: int) -> str:
        if index == 0:
            return 'a'
        elif index == 1:
            return 'b'
        else:
            return 'c'

    def find_next_char(char_index: int, n: int, start: int, end: int, k: int) -> None:
        nonlocal happy_string
        if n != 0:
            lower_index = -1
            upper_index = -1
            if char_index == 0:
                lower_index = 1
                upper_index = 2
            elif char_index == 1:
                lower_index = 0
                upper_index = 2
            else:
                lower_index = 0
                upper_index = 1
            midpoint = int((start + end) / 2)
            if k <= midpoint:
                happy_string += index_to_str(lower_index)
                find_next_char(lower_index, n - 1, start, midpoint, k)
            else:
                happy_string += index_to_str(upper_index)
                find_next_char(upper_index, n - 1, midpoint, end, k)

    poss_per_group = 2 ** (n - 1)
    group_num = math.ceil(k / poss_per_group) - 1
    happy_string = ''
    
    if k > poss_per_group * 3:
        return ''
    
    if group_num == 0:
        happy_string += 'a'
    elif group_num == 1:
        happy_string += 'b'
    else:
        happy_string += 'c'
    
    find_next_char(group_num, n - 1, group_num * poss_per_group, (group_num + 1) * poss_per_group, k)
    return happy_string