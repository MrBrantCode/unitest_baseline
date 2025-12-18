"""
QUESTION:
Given a number N.Your task is to print the no of divisors of number N which are perfect squares.
Example 1:
Input: 36
Output: 4
Explaination: The factors which are perfect 
square are 1, 4, 9 and 36.
Example 2:
Input: 60
Output: 2
Explaination: The factors which are perfect 
squares are 1 and 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function squareFactor() which takes N as input parameter and returns the count of the factors which are perfect squares.
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{12}
"""

def count_perfect_square_divisors(N: int) -> int:
    count = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % (i * i) == 0:
            count += 1
    return count