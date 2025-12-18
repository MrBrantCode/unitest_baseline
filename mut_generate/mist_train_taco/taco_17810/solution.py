"""
QUESTION:
Given two numbers X and N, find the smallest value of (N*K) which is closest to X. Where K is any positive number greater than zero. If in case there are two numbers closer to N, then return the larger number.
 
Example 1:
Input: X = 9, N = 2
Output: 10
Expalantion: 8 and 10 both are multiple of 2 and 
closest to 9, in this case we return the larger 
number that is 10.
Example 2:
Input: X = 2855, N = 13
Output: 2860
Explanation: 2860 is multiple of 13 and 
closest to 13.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function closestNo() which takes X and N as input parameter and return the number which is multiple of N and closest to X. In case of multiple numbers return the bigger one.
Expected Time Compelxity: O(1)
Expected Space Complexity: O(1)
Constraints:
1 <= X, N <= 1000000
"""

def closest_multiple(X: int, N: int) -> int:
    """
    Finds the multiple of N that is closest to X. If there are two multiples equally close, 
    returns the larger one.

    Parameters:
    X (int): The target number.
    N (int): The number whose multiple we are looking for.

    Returns:
    int: The multiple of N closest to X.
    """
    rem = X % N
    a = X - rem
    b = a + N
    
    if X - a < b - X and a != 0:
        return a
    else:
        return b