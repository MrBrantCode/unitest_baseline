"""
QUESTION:
You are given a string S consisting of lowercase English letters.
Determine whether we can turn S into a palindrome by repeating the operation of swapping two adjacent characters. If it is possible, find the minimum required number of operations.

-----Constraints-----
 - 1 \leq |S| \leq 2 × 10^5
 - S consists of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
If we cannot turn S into a palindrome, print -1. Otherwise, print the minimum required number of operations.

-----Sample Input-----
eel

-----Sample Output-----
1

We can turn S into a palindrome by the following operation:
 - Swap the 2-nd and 3-rd characters. S is now ele.
"""

def min_operations_to_palindrome(s: str) -> int:
    class Bit:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * n

        def sum(self, i):
            s = 0
            i -= 1
            while i >= 0:
                s += self.tree[i]
                i = (i & i + 1) - 1
            return s

        def add(self, i, x):
            while i < self.size:
                self.tree[i] += x
                i |= i + 1

    a = ord('a')

    def make_index(s):
        index = [[] for _ in range(26)]
        for (i, ch) in enumerate(s):
            index[ord(ch) - a].append(i)
        return index

    n = len(s)
    index = make_index(s)
    odd = None
    for (code, char_pos) in enumerate(index):
        if len(char_pos) % 2 == 1:
            if odd is not None:
                return -1
            odd = code

    bit = Bit(n)
    ans = 0
    cnt = 0
    for i in range(n):
        if bit.sum(i + 1) - bit.sum(i) == 1:
            continue
        code = ord(s[i]) - a
        if code == odd and index[code][-1] == i:
            continue
        cnt += 1
        j = index[code].pop()
        ans += n - cnt - (j - bit.sum(j))
        bit.add(j, 1)
        if n // 2 <= cnt:
            break

    if odd is not None:
        j = index[odd][-1]
        ans += abs(n // 2 - (j - bit.sum(j)))

    return ans