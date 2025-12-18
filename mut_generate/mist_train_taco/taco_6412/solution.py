"""
QUESTION:
Given a positive integer N. The problem is to print the numbers in the range 1 to n having bits in alternate pattern. Here alternate pattern means that the set and unset bits in the number occur in alternate order. For example- 5 has an alternate pattern i.e. 101.
Example 1:
Input:
N = 10
Output: 1 2 5 10
Explanation:
Binary representation of 1 : 0001
Binary representation of 2 : 0010
Binary representation of 5 : 0101
Binary representation of 10 : 1010
Here, We can see that the bits 
pattern in all the above configuration 
is alternate. So, we return an array
having {1, 2, 5 and 10}. 
 
Example 2:
Input:
N = 50
Output: 1 2 5 10 21 42
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printNumHavingAltBitPatrn() which takes the integer N as input parameters and returns an array of integers with alternate bits in the range 1 to N.
Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)
 
CONSTRAINTS:
1<= N <=10^{5}
"""

def printNumHavingAltBitPatrn(N):
    ans = []
    n = 1
    m = 0
    while n <= N:
        ans.append(n)
        n = (n << 1) + m
        m = 1 - m
    return ans