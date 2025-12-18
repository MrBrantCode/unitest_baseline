"""
QUESTION:
Given a string S which includes characters a, b, c, ..., z. Where value of a=1, b=2, ..., z=26. Now find the length of the largest increasing subsequence in the string.
Note:  Subsequence doesn't require elements to be consecutively increasing.
Example 1:
Input:
S = abcdapzfqh
Output:
6
Explanation:
The length of largest increasing
subsequence is 6. One of the
sequence with max length 6 is
a, b, c, d, p, z.
Example 2:
Input:
S = hkm 
Output:
3
Explanation:
The length of the largest increasing
subsequence is 3. Sequence with max
length 3 is h,k,m
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxLength() which take string S as input parameter and returns the length of the longest increasing subsequence.
Expected Time Complexity: O(|S|^{2}) 
Expected Space Complexity: O(|S|)
 
Constraints:
1<=|S|<=1000
"""

from bisect import bisect_left

def longest_increasing_subsequence_length(S: str) -> int:
    if not S:
        return 0
    
    arr = [S[0]]
    for item in S[1:]:
        if item > arr[-1]:
            arr.append(item)
        else:
            i = bisect_left(arr, item)
            arr[i] = item
    
    return len(arr)