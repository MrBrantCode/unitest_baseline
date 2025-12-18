"""
QUESTION:
Given a base B and a number N in that base, increment the number by one and print the resulting number in that base only.
 
Example 1:
Input:
B = 2
N = 0010
Output:
11
Explanation:
(0010)_{2} = (2)10
2 + 1 = 3
(3)_{10} = (11)2
Example 2:
Input:
B = 13
N = 2139
Output:
231A
Explanation:
(2319)_{13} = (81)10
81 + 1 = 82
(82)_{10} = (231A)_{13}
Your Task:
You don't need to read input or print anything. Your task is to complete the function inc() which takes an integer B, a string N as input parameter and returns the string by incrementing the number by one in the same base.
 
Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 
Constraints:
2 <= B <= 16
0000 <= N <= Max value in that base (e.g. 1111 for base 2, FFFF for base 16, etc.)
"""

def increment_in_base(B: int, N: str) -> str:
    # Convert the number from base B to decimal
    x = 0
    for i in range(len(N)):
        w = pow(B, i)
        c = 0
        if '0' <= N[len(N) - 1 - i] <= '9':
            c = int(ord(N[len(N) - 1 - i]) - ord('0'))
        else:
            c = int(ord(N[len(N) - 1 - i]) - ord('A') + 10)
        x = x + c * w
    
    # Increment the decimal number by 1
    x = x + 1
    
    # Convert the incremented decimal number back to base B
    ans = ''
    while x != 0:
        r = x % B
        c = '0'
        if r < 10:
            c = chr(int(r + ord('0')))
        else:
            c = chr(int(r - 10 + ord('A')))
        ans = c + ans
        x //= B
    
    return ans