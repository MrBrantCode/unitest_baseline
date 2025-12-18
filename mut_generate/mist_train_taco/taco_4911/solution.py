"""
QUESTION:
Given an integer N. The task is to count the number of integers from 1 to N(inclusive) which contain 0’s as a digit.
Example 1:
Input: N = 21
Output: 2
Explanation: All numbers are 10,20.
Ã¢â¬â¹Example 2:
Input: N = 101
Output: 11
Explanation: All numbers are 10,20
30,40,50,60,70,80,90,100,101.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countZero() which takes N as inputs and returns the answer.
Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N≤ 10^{6}
"""

def count_zeros_up_to_n(N: int) -> int:
    def zero_upto(digits: int) -> int:
        first = int((10 ** digits - 1) // 9)
        second = int((9 ** digits - 1) // 8)
        return (first - second) * 9

    sn = str(N)
    k = len(sn)
    nonzero = 0
    
    for i in range(k):
        if sn[i] == '0':
            nonzero -= 1
            break
        nonzero += (int(sn[i]) - 1) * 9 ** (k - 1 - i)
    
    no = 0
    remaining = 0
    count = 0
    
    for i in range(k):
        no = no * 10 + int(sn[i])
        if i != 0:
            count = count * 10 + 9
    
    remaining = no - count
    ans = zero_upto(k - 1) + (remaining - nonzero - 1)
    
    return ans