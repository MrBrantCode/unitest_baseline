"""
QUESTION:
Given a range from low to high and a number K. The task is to count the number which has the unit digit equal to K. 
 
Example 1:
Input:
low = 4, high = 9, K = 4 
Output:
1
Explanation:
4 is the only number with 4 as the
unit digit in the range of (4,9).
Example 2:
Input:
low = 3, high = 35, K = 3 
Output:
4
Explanation:
3, 13, 23, and 33 are the only numbers
with 3 as the unit digit in the given range.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countLastDigitK() which takes 3 Integers  low, high, and K as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= low <= high <= 10^{9}
0 <= K <= 9
"""

def count_numbers_with_unit_digit_k(low, high, K):
    # Calculate the number of full cycles of 10 in the range
    full_cycles = (high // 10) - (low // 10)
    
    # Check the unit digit of the lower bound
    lower_unit_digit = low % 10
    if lower_unit_digit > K:
        full_cycles -= 1
    
    # Check the unit digit of the upper bound
    upper_unit_digit = high % 10
    if upper_unit_digit >= K:
        full_cycles += 1
    
    return full_cycles