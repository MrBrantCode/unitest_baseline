"""
QUESTION:
Let's call a string good if its length is at least $2$ and all of its characters are ${A}$ except for the last character which is ${B}$. The good strings are ${AB},{AAB},{AAAB},\ldots$. Note that ${B}$ is not a good string.

You are given an initially empty string $s_1$.

You can perform the following operation any number of times:

Choose any position of $s_1$ and insert some good string in that position.

Given a string $s_2$, can we turn $s_1$ into $s_2$ after some number of operations?


-----Input-----

Each test contains multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single string $s_2$ ($1 \leq |s_2| \leq 2 \cdot 10^5$).

It is guaranteed that $s_2$ consists of only the characters ${A}$ and ${B}$.

It is guaranteed that the sum of $|s_2|$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print "YES" (without quotes) if we can turn $s_1$ into $s_2$ after some number of operations, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).


-----Examples-----

Input
4
AABAB
ABB
AAAAAAAAB
A
Output
YES
NO
YES
NO


-----Note-----

In the first test case, we transform $s_1$ as such: $\varnothing \to {{AAB}} \to {A}{{AB}}{AB}$.

In the third test case, we transform $s_1$ as such: $\varnothing \to {{AAAAAAAAB}}$.

In the second and fourth test case, it can be shown that it is impossible to turn $s_1$ into $s_2$.
"""

def can_transform_to_good_string(s2: str) -> bool:
    """
    Determines if the initially empty string s1 can be transformed into the given string s2
    by inserting good strings (strings that are at least length 2 and consist of 'A's followed by a 'B').

    Parameters:
    s2 (str): The target string to check.

    Returns:
    bool: True if s1 can be transformed into s2, False otherwise.
    """
    if s2[-1] != 'B':
        return False
    
    count_A = 0
    for char in s2:
        if char == 'A':
            count_A += 1
        else:
            if count_A == 0:
                return False
            count_A -= 1
    
    return True