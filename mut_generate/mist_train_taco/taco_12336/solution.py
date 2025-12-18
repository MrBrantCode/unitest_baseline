"""
QUESTION:
Given a number N, the task is to check whether the number is Trimorphic number or not. A number is called Trimorphic number if and only if its cube ends in the same digits as the number itself. In other words, number appears at the end of its cube i.e let's say if the number of digits of N is k then the last k digit of the cube should be equal to N only.
Example 1:
Input: N = 1
Output: 1
Explaination: 1^{3} = 1. So the cube here is ending with 
the number.
Example 2:
Input: N = 2
Output: 0
Explaination: 2^{3} = 8. The cube is not ending with the 
number at it's end.
Example 3:
Input: N = 24
Output: 1
Explaination: 24^{3} = 13824. The cube is ending with 24.
Your Task:
You do not need to read input or print anything, Your task is to complete the function isTrimorphic() which takes N as input parameter and returns 1 if the number is trimorphic, otherwise, returns 0.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 < N < 10000
"""

def is_trimorphic(N: int) -> int:
    c = N ** 3
    t = str(N)
    s = str(c)
    if s[-len(t):] == t:
        return 1
    else:
        return 0