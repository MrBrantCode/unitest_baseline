"""
QUESTION:
Given a series of numbers 2, 10, 30, 68, 130.., Identify the pattern in the series. You are given an integer X you need to find out the X'th number in the series.
Example 1:
Input:
X = 1
Output:
2
Explanation:
2 is the first number in the series.
Example 2:
Input:
X = 2
Output:
10
Explanation:
10 is the second number in the series.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function X1Series() which takes an integer X as an input parameter and return the X'th number in the series.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ X ≤ 10^{5}
"""

def X1Series(X: int) -> int:
    return pow(X, 3) + X