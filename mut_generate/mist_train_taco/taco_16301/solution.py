"""
QUESTION:
Find the number of days required to reach the top of the staircase of Q stairs if one moves R stairs upwards during daytime and S stairs downwards during night.
 
Example 1:
Input:
R = 5, S = 1, Q = 6
Output:
2
Explanation:
After end of whole first day he will
end up at Stair number 4. Then the next
day, he will reach the top by climbing 2
more stairs.
Example 2:
Input:
R = 2, S = 1, Q = 3
Output:
2
Explanation:
After end of whole first day he will
end up at Stair number 1. Then the next
day, he will reach the top by climbing 2
more stairs.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfDays() which takes 3 Integers R,S and Q as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= S < R <= Q <= 10^{9}
"""

import math

def calculate_days_to_reach_top(R: int, S: int, Q: int) -> int:
    """
    Calculate the number of days required to reach the top of the staircase.

    Parameters:
    R (int): Number of stairs moved upwards during the day.
    S (int): Number of stairs moved downwards during the night.
    Q (int): Total number of stairs to reach the top.

    Returns:
    int: Number of days required to reach the top of the staircase.
    """
    return math.ceil((Q - S) / (R - S))