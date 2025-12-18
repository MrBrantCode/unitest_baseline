"""
QUESTION:
Given a string arr consisting of lowercase english letters, arrange all its letters in lexicographical order using Counting Sort.
Example 1:
Input:
N = 5
S = "edsab"
Output:
abdes
Explanation: 
In lexicographical order, string will be 
abdes.
Example 2:
Input:
N = 13
S = "geeksforgeeks"
Output:
eeeefggkkorss
Explanation:
In lexicographical order, string will be 
eeeefggkkorss.
Your Task:
This is a function problem. You only need to complete the function countSort() that takes string arr as a parameter and returns the sorted string. The printing is done by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 10^{5}
Video:
"""

def count_sort_string(arr: str) -> str:
    cnt = [0] * 26
    for char in arr:
        cnt[ord(char) - 97] += 1
    sorted_string = ''
    for i in range(len(cnt)):
        while cnt[i] > 0:
            sorted_string += chr(i + 97)
            cnt[i] -= 1
    return sorted_string