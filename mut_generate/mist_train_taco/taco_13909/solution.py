"""
QUESTION:
Jon wants to go in birthday party of Arya. But he is busy in finding solution of crazy equations, so he wants your help to solve this problem. Jon has four integers a, b, c, d now he wants to calculate how many distinct set of x, y, z, w are present such that  a + b - x  == a + c - y == c + d - z == b + d - w
NOTE :  1<= x, y, z, w<=n   where n is a given integer.
Two set of x, y, z, w will be different if atleast one value will be different.
Example 1:
Input: n = 5, a = 1, b = 2, c = 2, d = 2
Output: 4
Explanation: Sets of x, y, z, w can be
             (1, 1, 2, 2)
             (2, 2, 3, 3)
             (3, 3, 4, 4)
             (4, 4, 5, 5).
Example 2:
Input: n = 5, a = 1, b = 2, c = 2, d = 1
Output: 5
Explanation: same explanation as previous one.
Your Task:  
You dont need to read input or print anything. Complete the function distinctValues() which takes n, a, b, c and d as input parameter and returns the total number of distinct set of x, y, z, w are present. 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 <= n <= 10^{6}
1 <= a, b, c, d <= n
"""

def distinct_values(n, a, b, c, d):
    arr = [a + b, a + c, c + d, b + d]
    arr.sort()
    diff = arr[-1] - arr[0]
    return max(n - diff, 0)