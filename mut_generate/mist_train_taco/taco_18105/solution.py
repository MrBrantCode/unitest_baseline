"""
QUESTION:
Given a non-negative number n and two values l and r. The problem is to count the number of unset bits in the range l to r in the binary representation of n, i.e. to count unset bits from the rightmost lth bit to the rightmost rth bit.
 
Example 1:
Input:
n = 42, l = 2, r = 5
Output:
2
Explanation:
(42)_{10} = (101010)_{2}
There are '2' unset bits in the range 2 to 5.
Example 2:
Input:
n = 80, l = 1, r = 4
Output:
4
Explanation:
(80)_{10} = (1010000)_{2}
There are '4' unset bits in the range 1 to 4.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function countUnsetBits() which takes 3 Integers n, a, and b as input and returns the count of unset bits in the given range of [l, r].
 
Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= n <= 10^{5}
1 <= l <= r <= 17
"""

def count_unset_bits(n: int, l: int, r: int) -> int:
    # Convert the number to binary and reverse it to align with 1-based indexing
    binary = bin(n).replace('0b', '')[::-1]
    
    # Extract the substring from l-1 to r (inclusive) and count the '0's
    ans = binary[l - 1:r].count('0')
    
    return ans