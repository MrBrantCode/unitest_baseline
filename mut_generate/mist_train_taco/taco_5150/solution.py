"""
QUESTION:
Given a number N. Check whether it is a magic number or not.
Note:- A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition and the single digit comes out to be 1.
Example 1:
Input: N = 1234
Output: 1
Explanation: 1 + 2 + 3 + 4 = 10, 
Again 1 + 0 = 1. Thus, 1234 is a magic 
number. 
Example 2:
Input: N = 1235
Output: 0
Explanation: 1 + 2 + 3 + 5 = 11. Again, 
1 + 1 = 2. Thus, 1235 is not a magic number.
Your Task:
You don't need to read input or print anything.Your task is to complete the function isMagic() which takes a number N as input parameter and returns 1 if the number is a magic number.Otherwise, it returns 0.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

def is_magic_number(N: int) -> int:
    if N < 9:
        if N == 1:
            return 1
        else:
            return 0
    while N >= 10:
        summ = 0
        while N > 0:
            rem = N % 10
            summ += rem
            N = N // 10
        N = summ
    if summ == 1:
        return 1
    return 0