"""
QUESTION:
Given a number S(in the form of a string). Count all the digits in S which divide S. Divisibility by 0 is not allowed. If any digit in S which is repeated divides S, then all repetitions of that digit should be counted.
Example 1:
Input:
S = "35"
Output:
1
Explanation:
Only 5 digits 35,thus the answer is 1.
Example 2:
Input:
S = "1122324"
Output:
7
Explanation:
All the digits divide 1122324, therefore,
the answer is 7.
Your Task:
You don't need to read input or print anything.Your task is to complete the function divisibleByDigits()  which takes the number S(in the form of a string) as input parameter and returns the number of digits of S that divide S.
Expected Time Complexity: O(N)
Expected Auxillary Space: O(constant)
Constraints:
1<=|S|<=10^{6}
"""

def count_divisible_digits(S: str) -> int:
    c = 0
    d = {}
    a = int(S)
    s = set()
    
    for i in S:
        if i not in d:
            d[i] = 0
            if i != '0' and a % int(i) == 0:
                s.add(i)
        d[i] += 1
    
    for i in s:
        c += d[i]
    
    return c