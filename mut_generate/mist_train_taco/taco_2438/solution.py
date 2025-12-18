"""
QUESTION:
You are given four integer values $a$, $b$, $c$ and $m$.

Check if there exists a string that contains:

$a$ letters 'A';

$b$ letters 'B';

$c$ letters 'C';

no other letters;

exactly $m$ pairs of adjacent equal letters (exactly $m$ such positions $i$ that the $i$-th letter is equal to the $(i+1)$-th one).


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of testcases.

Each of the next $t$ lines contains the description of the testcase — four integers $a$, $b$, $c$ and $m$ ($1 \le a, b, c \le 10^8$; $0 \le m \le 10^8$).


-----Output-----

For each testcase print "YES" if there exists a string that satisfies all the requirements. Print "NO" if there are no such strings.

You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes and YES will all be recognized as positive answer).


-----Examples-----

Input
3
2 2 1 0
1 1 1 1
1 2 3 2
Output
YES
NO
YES


-----Note-----

In the first testcase strings "ABCAB" or "BCABA" satisfy the requirements. There exist other possible strings.

In the second testcase there's no way to put adjacent equal letters if there's no letter that appears at least twice.

In the third testcase string "CABBCC" satisfies the requirements. There exist other possible strings.
"""

def can_form_string(a: int, b: int, c: int, m: int) -> str:
    curSum = a + b + c
    x = curSum // 2 + curSum % 2
    maxiumu = a - 1 + b - 1 + c - 1
    minPos = 0
    
    if a > x:
        if curSum % 2 != 0:
            minPos = 2 * (a - x)
        else:
            minPos = 2 * (a - x - 1) + 1
    elif b > x:
        if curSum % 2 != 0:
            minPos = 2 * (b - x)
        else:
            minPos = 2 * (b - x - 1) + 1
    elif c > x:
        if curSum % 2 != 0:
            minPos = 2 * (c - x)
        else:
            minPos = 2 * (c - x - 1) + 1
    
    if m <= maxiumu and m >= minPos:
        return "YES"
    else:
        return "NO"