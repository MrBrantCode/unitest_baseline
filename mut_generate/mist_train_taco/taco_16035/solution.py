"""
QUESTION:
You are given a string S containing only lowercase characters. 
You can rearrange the string and you have to print minimum number of characters needed(can be 0) to make it palindrome.

-----Input:-----
- First line contain an interger T denoting number of testcases.
- First line of each testcase contains integer N, size of string.
- Second line of each testcase contains string S.

-----Output:-----
For each test case, print a single line containing one integer ― the minimum number of characters needed(can be 0) to make it palindrome.

-----Constraints-----
- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$

-----Sample Input:-----
3
1
a
9
abbbcbddd
6
abcdef

-----Sample Output:-----
0
2
5

-----EXPLANATION:-----
- Example case 1: a is already a palindrome.
- Example case 2: abbddcddbba is palindrome by adding 2 more characters.
- Example case 3: abdefcfedba is palindrome by adding 5 more characters.
"""

from collections import Counter

def min_chars_to_palindrome(S: str) -> int:
    counts = Counter(S)
    odd_counts = 0
    for count in counts.values():
        odd_counts += count % 2
    return max(odd_counts - 1, 0)