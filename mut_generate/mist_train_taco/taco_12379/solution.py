"""
QUESTION:
Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A. If B cannot be a substring of A no matter how many times it is repeated, return -1.
Example 1:
Input: A = "abcd", B = "cdabcdab"
Output: 3
Explanation: After repeating A three times, 
we get "abcdabcdabcd".
Example 2:
Input: A = "aa", B = "a"
Output: 1
Explanation: B is already a substring of A.
Your Task:  
You don't need to read input or print anything. Complete the function repeatedStringMatch() which takes strings A and B as input parameters and returns the minimum number of operations to complete the task. If it is not possible then return -1.
Expected Time Complexity: O(|A| * |B|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |A|, |B| ≤ 4 * 10^{3}
"""

from math import ceil

def repeated_string_match(a: str, b: str) -> int:
    if b in a:
        return 1
    n = len(a)
    m = len(b)
    count = ceil(m / n)
    if b in count * a:
        return count
    elif b in (count + 1) * a:
        return count + 1
    else:
        return -1