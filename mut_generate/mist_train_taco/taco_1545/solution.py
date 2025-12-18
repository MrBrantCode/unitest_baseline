"""
QUESTION:
Given an integer N, find the absolute difference between sum of the squares of first N natural numbers and square of sum of first N natural numbers.
Example 1:
Input: N = 2
Output: 4 
Explanation: abs|(1^{2 }+ 2^{2}) - (1 + 2)^{2}| = 4.
Example 2:
Input: N = 3
Output: 22
Explanation: abs|(1^{2 }+ 2^{2} + 3^{2}) - (1 + 2 + 3)^{2}| = 22.
Your Task:  
You dont need to read input or print anything. Complete the function squaresDiff() which takes N as input parameter and returns the absolute difference.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{3}
"""

def calculate_squares_diff(N: int) -> int:
    sum_of_squares = sum(i ** 2 for i in range(1, N + 1))
    sum_of_numbers = sum(i for i in range(1, N + 1))
    square_of_sum = sum_of_numbers ** 2
    return abs(sum_of_squares - square_of_sum)