"""
QUESTION:
Given a string consisting of only numbers from 0 to 9, consider the operation of creating a new string from that string according to the following rules. Read the given string one character at a time from the left end. Go, if the same number a continues r, write the number r and the number a in this order without separating them with a space. Read to the right end of the given character string, and what is on the way to the end of the last writing Even if there are times of writing, all of them are counted as one operation. For the second and subsequent operations, the same operation is performed with the character string written out by the previous operation as the given character string. For example, "122244" If the character string "" is given, the character string obtained by one operation is "113224" and "44444444444" (11) because one 1, three 2, two 4s are given in order from the left end. In the case of 4), the obtained character string is “114”.

Create a program that outputs a string obtained by performing the above operation n times on a given string of 100 characters or less, where n ≤ 20.

The input data consists of two lines, the first line contains the number of operations n, and the second line contains the first character string.

Input example
---
Five
11
Output example
13112221

input

The input consists of multiple datasets. Input ends when n is 0. The number of datasets does not exceed 5.

output

For each data set, the character string that has been operated the specified number of times is output on one line.





Example

Input

5
11
5
11
0


Output

13112221
13112221
"""

def perform_operations(initial_string: str, n: int) -> str:
    def change(x: list) -> list:
        i = 0
        ans = []
        while i < len(x):
            cnt = 1
            j = 1
            while i + j < len(x) and x[i + j] == x[i]:
                cnt += 1
                j += 1
            ans.extend([str(cnt), x[i]])
            i += cnt
        return ans

    lst = list(initial_string)
    for _ in range(n):
        lst = change(lst)
    return ''.join(lst)