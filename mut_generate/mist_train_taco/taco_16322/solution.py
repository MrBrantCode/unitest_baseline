"""
QUESTION:
The jet's speed is changed after every mile covered on it's runway. It follows a specific pattern for the speed. Starting from 1 it goes like 1, 7, 16, 21, 81, 63, 256 . . .  and so on. Given N find its speed after Nth mile.
 
Example 1:
Input : N = 3
Output: 16
Explanation: Speed of jet after 3rd mile
is 16.
Example 2:
Input: N = 5
Output: 81
Explanation: Speed of jet after 5th mile 
is 81.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function Nth_mileSpeed() which taked N as input parameter and returns jet's speed after Nth mile.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 60
"""

def Nth_mileSpeed(n: int) -> int:
    if n % 2 != 0:
        return (n - n // 2) ** 4
    else:
        return 7 * 3 ** (n // 2 - 1)