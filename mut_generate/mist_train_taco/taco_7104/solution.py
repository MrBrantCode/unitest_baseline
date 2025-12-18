"""
QUESTION:
One day in the IT lesson Anna and Maria learned about the lexicographic order.

String x is lexicographically less than string y, if either x is a prefix of y (and x ≠ y), or there exists such i (1 ≤ i ≤ min(|x|, |y|)), that xi < yi, and for any j (1 ≤ j < i) xj = yj. Here |a| denotes the length of the string a. The lexicographic comparison of strings is implemented by operator < in modern programming languages​​.

The teacher gave Anna and Maria homework. She gave them a string of length n. They should write out all substrings of the given string, including the whole initial string, and the equal substrings (for example, one should write out the following substrings from the string "aab": "a", "a", "aa", "ab", "aab", "b"). The resulting strings should be sorted in the lexicographical order. The cunning teacher doesn't want to check all these strings. That's why she said to find only the k-th string from the list. Help Anna and Maria do the homework.

Input

The first line contains a non-empty string that only consists of small Latin letters ("a"-"z"), whose length does not exceed 105. The second line contains the only integer k (1 ≤ k ≤ 105).

Output

Print the string Anna and Maria need — the k-th (in the lexicographical order) substring of the given string. If the total number of substrings is less than k, print a string saying "No such line." (without the quotes).

Examples

Input

aa
2


Output

a


Input

abc
5


Output

bc


Input

abab
7


Output

b

Note

In the second sample before string "bc" follow strings "a", "ab", "abc", "b".
"""

from heapq import heappop, heappush, heapify

def find_kth_lexicographical_substring(s: str, k: int) -> str:
    n = len(s)
    if k > n * (n + 1) / 2:
        return 'No such line.'
    
    ss = [(s[i], i) for i in range(n)]
    heapify(ss)
    
    while k > 0:
        k -= 1
        t = heappop(ss)
        if k == 0:
            return t[0]
        elif t[1] < n - 1:
            heappush(ss, (t[0] + s[t[1] + 1], t[1] + 1))
    
    return 'No such line.'