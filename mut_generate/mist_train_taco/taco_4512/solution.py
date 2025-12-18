"""
QUESTION:
A pair of strings $(α, β)$ is called a subpair of a string $x$ if $x$ = $x_1+$$α+$$x_2+$$β+$$x_3$ (where a+b means concatenation of strings a and b) for some (possibly empty) strings $x1, x2$ and $x3$. We are given two strings and we need to find one subpair from each string such that : 
Let $(a,b) , (c,d) $be subpair of $string1$ and $string2$ respectively and $X$ $=$ $a$ + $b$ + $c$ + $d$
- $X$ is a palindrome
- $|a| = |d|$
- $|b| = |c|$
- $|X|$ is maximum

-----Input Format:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, two strings str1, str2. 

-----Output Format:-----
- For each testcase, output in a single line representing the length of palindrome |X|.

-----Constraints-----
- $1 \leq T \leq 5$
- $2 \leq |str1| \leq 10^3$
- $2 \leq |str2| \leq 10^3$

-----Sample Input 1:-----
1
abgcd dchbag

-----Sample Output 1:-----
8

-----Sample Input 2:-----
4   

aaa aaa

zaaax yaaaw

zax yaw

zx yw

-----Sample Output 2:-----
6

6

2

0  

-----EXPLANATION:-----
Sample Testcase 1: The subpairs are ("ab","cd") and ("dc","ba"). When the subpairs are concatenated string is "abcddcba" which is a pallindrome , |"ab"| = |"ba"|, |"cd"| = |"dc"| and has the maximum length equal to 8.
"""

from collections import defaultdict as dd

def find_max_palindrome_length(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # Reverse str2 to facilitate palindrome checking
    str2 = str2[::-1]
    
    # Initialize the DP table
    dp = [[0] * (m + 1) for i in range(n + 1)]
    
    # Fill the DP table
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
    
    # Initialize a defaultdict to store maximum values
    mx = dd(int)
    ans = 0
    
    # Fill the mx dictionary
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            a = mx[i + 1, j]
            b = mx[i, j + 1]
            mx[i, j] = max([dp[i][j], a, b])
    
    # Calculate the maximum length of the palindrome
    for i in range(n):
        for j in range(m):
            c = dp[i][j]
            nxt = mx[i + c, j + c]
            cur = c + nxt
            ans = max(ans, cur)
    
    # Return the maximum length of the palindrome
    return 2 * ans