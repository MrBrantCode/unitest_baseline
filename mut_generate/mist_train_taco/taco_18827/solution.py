"""
QUESTION:
Given a number N.Find the nearest number which is a power of 2 and greater than or equal to N.
Example 1:
Input:
N = 1
Output:
1
Explanation:
The nearest power of 2 greater than or 
equal to 1 is 2^0=1.
Example 2:
Input:
N = 5
Output:
8
Explanation:
The nearest power of 2 greater than 5 is 
2^3=8.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function nearestPowerOf2() which takes a number N as input parameter and returns the nearest power of 2 that is greater than or equal to N.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{18}
"""

def nearest_power_of_2(N: int) -> int:
    count = 0
    n = N
    
    # Check if N is already a power of 2
    if n & (n - 1) == 0:
        return N
    
    # Find the highest bit set in N
    while n != 0:
        count += 1
        n >>= 1
    
    # The nearest power of 2 greater than or equal to N
    return 1 << count