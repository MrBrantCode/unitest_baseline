"""
QUESTION:
Given a number N, count the numbers from 1 to N that don’t contain digit 3 in their decimal representation.
 
Example 1:
Input:
N = 5
Output:
4
Explanation:
From 1 - 5, only 3 contains
3 in its decimal representation
so output is 4
Example 2:
Input:
N = 25
Output:
22
Explanation:
In between 1 to 25,
3,13,23 contain 3 in their
decimal representaion so 
output is 25 - 3 = 22
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which takes an integer N as input parameter and returns an integer, the total count of numbers from 1 to N that don’t contain digit 3 in their decimal representation.
 
Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 
Constraints:
0 <= N <= 500
"""

def count_numbers_without_digit_3(N: int) -> int:
    count = 0
    for i in range(1, N + 1):
        if '3' not in str(i):
            count += 1
    return count