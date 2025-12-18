"""
QUESTION:
Description
You are given two strings S and T, such that length of S is greater than the length of T.
Then a substring of S is defined as a sequence of characters which appear consecutively in S.

Find the total number of distinct substrings of M such that T is a substring of M

Input Format
One line containing strings S and T separated by a space.

Output Format
One line containing the number of distinct substrings of M such that T is a substring of M

Input Limits:
0 < Length(S), Length(T) < 100

SAMPLE INPUT
abcc c

SAMPLE OUTPUT
6

Explanation

Suppose  the  string  S  is  abcc.  Then  the  distinct  substrings  of  S  are
a, b, c, ab, bc, cc, abc, bcc, abcc
"""

def count_substrings_containing_t(S: str, T: str) -> int:
    def get_all_substrings(string: str) -> list:
        length = len(string)
        alist = []
        for i in range(length):
            for j in range(i, length):
                substring = string[i:j + 1]
                if substring not in alist:
                    alist.append(substring)
        return alist
    
    all_substrings = get_all_substrings(S)
    count = 0
    for substring in all_substrings:
        if T in substring:
            count += 1
    return count