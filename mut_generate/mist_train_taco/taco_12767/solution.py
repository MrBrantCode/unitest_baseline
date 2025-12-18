"""
QUESTION:
Let's define a multiplication operation between a string $a$ and a positive integer $x$: $a \cdot x$ is the string that is a result of writing $x$ copies of $a$ one after another. For example, "abc" $\cdot~2~=$ "abcabc", "a" $\cdot~5~=$ "aaaaa".

A string $a$ is divisible by another string $b$ if there exists an integer $x$ such that $b \cdot x = a$. For example, "abababab" is divisible by "ab", but is not divisible by "ababab" or "aa".

LCM of two strings $s$ and $t$ (defined as $LCM(s, t)$) is the shortest non-empty string that is divisible by both $s$ and $t$.

You are given two strings $s$ and $t$. Find $LCM(s, t)$ or report that it does not exist. It can be shown that if $LCM(s, t)$ exists, it is unique.


-----Input-----

The first line contains one integer $q$ ($1 \le q \le 2000$) — the number of test cases.

Each test case consists of two lines, containing strings $s$ and $t$ ($1 \le |s|, |t| \le 20$). Each character in each of these strings is either 'a' or 'b'.


-----Output-----

For each test case, print $LCM(s, t)$ if it exists; otherwise, print -1. It can be shown that if $LCM(s, t)$ exists, it is unique.


-----Examples-----

Input
3
baba
ba
aa
aaa
aba
ab
Output
baba
aaaaaa
-1


-----Note-----

In the first test case, "baba" = "baba" $\cdot~1~=$ "ba" $\cdot~2$.

In the second test case, "aaaaaa" = "aa" $\cdot~3~=$ "aaa" $\cdot~2$.
"""

import math

def find_lcm_of_strings(s: str, t: str) -> str:
    """
    Finds the Least Common Multiple (LCM) of two strings s and t.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        str: The LCM of the two strings if it exists, otherwise '-1'.
    """
    sb = ''
    k = 0
    
    # Find the smallest common substring that can be repeated to form both s and t
    for i in range(1, min(len(s), len(t)) + 1):
        if len(s) % i == 0 and len(t) % i == 0:
            sub = s[0:i]
            if s == sub * (len(s) // i) and t == sub * (len(t) // i):
                sb = sub
                k = i
                break
    
    # If no common substring was found, return -1
    if sb == '':
        return '-1'
    
    # Calculate the LCM of the lengths of the strings when divided by k
    a = len(s) // k
    b = len(t) // k
    lcm_length = a * b // math.gcd(a, b)
    
    # Return the LCM string
    return sb * lcm_length