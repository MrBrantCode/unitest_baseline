"""
QUESTION:
Given an array A of n integers, the task is to count the number of ways to split given array elements into two disjoint groups such that XOR of elements of each group is equal.
Note: The answer could be very large so print it by doing modulos with 10^{9} + 7. 
Example 1:
Input : a[] = {1, 2, 3}
Output : 3
Explanation:
{(1),(2, 3)},{(2),(1, 3)},{(3),(1, 2)}
are three ways with equal XOR
value of two groups.
Example 2:
Input : a[] = {5, 2, 3, 2}
Output : 0
Your Task:
The input is already taken care of by the driver code. You only need to complete the function countgroup() that takes an array (a), sizeOfArray (n), and return the number of ways to split an array. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1<=N<=10^{5}
1<=a<=10^{8}
"""

def count_equal_xor_groups(a, n):
    xor = 0
    for i in a:
        xor ^= i
    
    if xor != 0:
        return 0
    
    return (pow(2, n - 1, 1000000007) - 1) % 1000000007