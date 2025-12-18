"""
QUESTION:
Given three numbers a, b and m. The task is to find (a^b)%m.
Note: a is given as a String because it can be very big.
 
Example 1:
Input:
a = "3", b = 2, m = 4
Output:
1
Explanation:
(3^2)%4 = 9%4 = 1
Example 2:
Input:
a = "8", b = 2, m = 6
Output:
4
Explanation:
(8^2)%6 = 64%6 = 4 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function powerMod() which takes a string a and 2 integers b, and m as input and returns (a^{b} % m).
 
Expected Time Complexity: O(Number of digits in a)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |a| <= 10^{5}
0 <= b <= 10^{9}
1 <= m <=10^{9}
"""

def power_mod(a: str, b: int, m: int) -> int:
    """
    Calculate (a^b) % m where a is given as a string because it can be very big.

    Parameters:
    a (str): The base number as a string.
    b (int): The exponent.
    m (int): The modulus.

    Returns:
    int: The result of (a^b) % m.
    """
    return pow(int(a), b, m)