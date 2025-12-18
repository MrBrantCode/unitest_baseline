"""
QUESTION:
Given two integers X and K. The task is to find smallest K-digit number divisible by X.
Note:  It is given that number of digits in X is always smaller or equal to K.
 
Example 1:
Input:
X = 6, K = 1
Output:
6
Explanation:
6 is the smallest 1 digit number
which is divisible by 6.
Example 2:
Input:
X = 5, K = 2
Output:
10
Explanation:
10 is the smallest 2 digit number
which is divisible by 5.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestKDigitNum() which takes 2 Integers X and K as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= X <= 10^{5}
1 <= K <= 18
"""

def smallest_k_digit_num(X: int, K: int) -> int:
    # Calculate the smallest K-digit number
    Min = 10 ** (K - 1)
    
    # Check if this number is divisible by X
    if Min % X == 0:
        return Min
    else:
        # If not, find the next number divisible by X
        return Min + X - (Min % X)