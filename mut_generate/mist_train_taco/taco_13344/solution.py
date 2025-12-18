"""
QUESTION:
You are given 2 numbers (n , m); the task is to find ^{n}√m (n^{th} root of m).
 
Example 1:
Input: n = 2, m = 9
Output: 3
Explanation: 3^{2} = 9
Example 2:
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not
integer.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function NthRoot() which takes n and m as input parameter and returns the nth root of m. If the root is not integer then returns -1.
 
Expected Time Complexity: O(n* log(m))
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 30
1 <= m <= 10^{9}
"""

def find_nth_root(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        if pow(mid, n) == m:
            return mid
        if pow(mid, n) < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1