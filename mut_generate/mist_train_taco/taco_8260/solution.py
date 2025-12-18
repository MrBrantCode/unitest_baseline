"""
QUESTION:
Given a large number (represented as string S)  which has to divided by another number (represented as int data type D). The task is to find division of these numbers.
Example 1:
Input: S = "123456" , D = 36
Output: 3429
Explanation: simply S/D = 3429
Example 2:
Input: S = "91345243" , D = 67
Output: 1363361
Explanation: S/D = 1363361
Your Task:  
You don't need to read input or print anything. Your task is to complete the function longDivision() which accepts a string S and an integer divisor D as input parameter and returns a string.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5 }
"""

def long_division(S: str, D: int) -> str:
    """
    Perform long division of a large number represented as a string by an integer divisor.

    Parameters:
    S (str): The large number to be divided, represented as a string.
    D (int): The integer divisor.

    Returns:
    str: The result of the division, represented as a string.
    """
    S = int(S)
    divide = S // D
    return str(divide)