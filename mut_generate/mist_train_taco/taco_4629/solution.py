"""
QUESTION:
Given a string, the task is to find whether it contains an additive sequence or not. A string contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers. You are required to complete the function which returns true if the string is a valid sequence else returns false.
Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow . Each test case contains a string s .
Output:
For each test case in a new line output will be 1 if it contains an additive sequence and 0 if it doesn't contains an additive sequence.
Constraints:
1<=T<=100
1<=length of string<=200
Example:
Input
3
1235813
1711
199100199
Output
1
0
1
Explanation:
1. In first test case series will be (1 2 3 5 8 13 ) as 1+2=3, 2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13 .
2. In the second test case there is no such series possible.
3. In the third test case there is the series will be 1 99 100 199 .
Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.
"""

def is_additive_sequence(num: str) -> bool:
    def solve(a: int, b: int, s: str, k: int, n: int, start: int = 0) -> int:
        if k == n and start > 0:
            return 1
        for i in range(1, n):
            if k + i > n:
                break
            c = int(s[k:k + i])
            if c == a + b:
                return solve(b, c, s, k + i, n, start + 1)
            elif c > a + b:
                return 0
        return 0

    n = len(num)
    for i in range(1, n):
        for j in range(1, n):
            a = int(num[0:i])
            b = int(num[i:i + j])
            if solve(a, b, num, i + j, n):
                return True
    return False