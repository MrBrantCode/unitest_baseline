"""
QUESTION:
Given a single integer N, your task is to find the sum of the square of the first N odd natural Numbers.
 
Example 1:
Input: 2
Output: 10
Explanation: 1^{2 + }3^{2}^{ }= 10
Example 2: 
Input: 3
Output: 35
Explanation: 1^{2} + 3^{2} + 5^{2} = 35
 
Your Task:
You don't need to read or print anything. Your task is to complete the function sum_of_square_oddNumbers() which takes N as the input parameter and returns the sum of the first N odd natural numbers.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10000
"""

def sum_of_square_odd_numbers(N: int) -> int:
    total = 0
    for i in range(1, 2 * N, 2):
        total += i ** 2
    return total