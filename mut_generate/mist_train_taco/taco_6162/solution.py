"""
QUESTION:
You are provided an unlimited collection of red, green and blue balls. Now your task is to arrange N balls taken from this collection in a line in such a way that red balls appear first, followed by green balls and then blue balls. Given a value of N you have to find the number of ways to do that.
Note:  In a particular arrangement a certain color of balls may be missing but the order must be strictly maintained with the available balls.
 
 
Example 1:
Input:
N = 1
Output:
3
Explanation:
You are allowed to take 1 
ball only. So that one ball 
can be red, green, or blue. 
So the number of ways, in 
this case is 3.
 
Example 2:
Input:
N = 2
Output:
6
Explanation:
You are allowed to take 2 
balls. So you have six 
alternative arrangements ie. 
RG,GB,RB,RR,GG,BB.
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numberOfWays() which takes an integer N and returns the number of ways to do that.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints 
1<=N<=10^9
"""

def calculate_ball_arrangements(N: int) -> int:
    """
    Calculate the number of ways to arrange N balls in a line such that red balls appear first, 
    followed by green balls, and then blue balls.

    Parameters:
    N (int): The number of balls to be arranged.

    Returns:
    int: The number of ways to arrange the balls.
    """
    return (N + 1) * (N + 2) // 2