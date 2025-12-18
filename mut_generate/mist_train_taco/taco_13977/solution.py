"""
QUESTION:
Given a number N.Find the minimum Lucky number, the sum of whose digits is equal to N.
Note:-Lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. 
Example 1:
Input:
N=29
Output:
44777
Explanation:
44777 is the smallest number whose 
digit-sum(4+4+7+7+7) is equal to 29.
Example 2:
Input:
N=9
Output:
-1
Explanation:
There is no lucky number whose digit-sum
is equal to 9.
Your Task:
You don't need to read input or print anything.Your task is to complete the function minimumLuckyNumber() which takes a number N as input parameters and returns the minimum Lucky number(in the form of a string) whose digit-sum is equal to N. If there is no lucky number whose digit-sum is equal to N, then return -1.
Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{5}
^{Note:The answer may not fit in 64 bit integer representations.}
"""

def minimum_lucky_number(N: int) -> str:
    a, b = 0, 0
    while N > 0:
        if N % 7 == 0:
            a += 1
            N -= 7
        else:
            b += 1
            N -= 4
    
    if N < 0:
        return '-1'
    
    return '4' * b + '7' * a