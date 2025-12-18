"""
QUESTION:
"Everything in the universe is balanced. Every disappointment you face in life will be balanced by something good for you! Keep going, never give up."
Let's call a string balanced if all characters that occur in this string occur in it the same number of times.
You are given a string $S$; this string may only contain uppercase English letters. You may perform the following operation any number of times (including zero): choose one letter in $S$ and replace it by another uppercase English letter. Note that even if the replaced letter occurs in $S$ multiple times, only the chosen occurrence of this letter is replaced.
Find the minimum number of operations required to convert the given string to a balanced string.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

-----Output-----
For each test case, print a single line containing one integer ― the minimum number of operations.

-----Constraints-----
- $1 \le T \le 10,000$
- $1 \le |S| \le 1,000,000$
- the sum of $|S|$ over all test cases does not exceed $5,000,000$
- $S$ contains only uppercase English letters

-----Subtasks-----
Subtask #1 (20 points):
- $T \le 10$
- $|S| \le 18$
Subtask #2 (80 points): original constraints

-----Example Input-----
2
ABCB
BBC

-----Example Output-----
1
1

-----Explanation-----
Example case 1: We can change 'C' to 'A'. The resulting string is "ABAB", which is a balanced string, since the number of occurrences of 'A' is equal to the number of occurrences of 'B'.
Example case 2: We can change 'C' to 'B' to make the string "BBB", which is a balanced string.
"""

from collections import Counter

def factors(n):
    p = min(n + 1, 27)
    return [[i, n // i] for i in range(1, p) if n % i == 0]

def balance(s, x, typ, count):
    l = len(x)
    if l == typ:
        y = [i - count for i in x]
        y = [_ for _ in y if _ > 0]
        return sum(y)
    if l < typ:
        d = typ - l
        x.extend([0] * d)
        return balance(s, x, typ, count)
    if l > typ:
        y = sum(x[typ:])
        z = 0
        m = typ - 1
        while y:
            n = count - x[m]
            if n <= y:
                y -= n
            else:
                n = y
                y = 0
            z += n
            x[m] = x[m] + n
            m -= 1
        return z + balance(s, x[:typ], typ, count)

def min_operations_to_balance_string(S):
    l = len(S)
    c = Counter(S)
    x = sorted(c.values())[::-1]
    r = [balance(S, x[:], typ, count) for (typ, count) in factors(l)]
    return min(r)