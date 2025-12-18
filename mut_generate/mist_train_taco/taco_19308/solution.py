"""
QUESTION:
You are given a string $s$. You have to determine whether it is possible to build the string $s$ out of strings aa, aaa, bb and/or bbb by concatenating them. You can use the strings aa, aaa, bb and/or bbb any number of times and in any order.

For example:

aaaabbb can be built as aa $+$ aa $+$ bbb;

bbaaaaabbb can be built as bb $+$ aaa $+$ aa $+$ bbb;

aaaaaa can be built as aa $+$ aa $+$ aa;

abab cannot be built from aa, aaa, bb and/or bbb.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases.

Each test case consists of one line containing the string $s$ ($1 \le |s| \le 50$), consisting of characters a and/or b.


-----Output-----

For each test case, print YES if it is possible to build the string $s$. Otherwise, print NO.

You may print each letter in any case (for example, YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).


-----Examples-----

Input
8
aaaabbb
bbaaaaabbb
aaaaaa
abab
a
b
aaaab
bbaaa
Output
YES
YES
YES
NO
NO
NO
NO
YES


-----Note-----

The first four test cases of the example are described in the statement.
"""

def can_build_from_substrings(s: str) -> str:
    """
    Determines whether the string `s` can be built from the substrings "aa", "aaa", "bb", and "bbb".

    Parameters:
    s (str): The string to be checked.

    Returns:
    str: "YES" if the string can be built, otherwise "NO".
    """
    if len(s) < 2:
        return 'NO'
    
    arr = []
    curr = 1
    last = s[0]
    
    for i in range(1, len(s)):
        if s[i] == last:
            curr += 1
        else:
            arr.append(curr)
            curr = 1
            last = s[i]
    arr.append(curr)
    
    for count in arr:
        if count < 2:
            return 'NO'
    
    return 'YES'