"""
QUESTION:
For each string s consisting of characters '0' and '1' one can define four integers a_00, a_01, a_10 and a_11, where a_{xy} is the number of subsequences of length 2 of the string s equal to the sequence {x, y}. 

In these problem you are given four integers a_00, a_01, a_10, a_11 and have to find any non-empty string s that matches them, or determine that there is no such string. One can prove that if at least one answer exists, there exists an answer of length no more than 1 000 000.


-----Input-----

The only line of the input contains four non-negative integers a_00, a_01, a_10 and a_11. Each of them doesn't exceed 10^9.


-----Output-----

If there exists a non-empty string that matches four integers from the input, print it in the only line of the output. Otherwise, print "Impossible". The length of your answer must not exceed 1 000 000.


-----Examples-----
Input
1 2 3 4

Output
Impossible

Input
1 2 2 1

Output
0110
"""

import math

def find_matching_string(a_00, a_01, a_10, a_11):
    def is_square(integer):
        root = math.sqrt(integer)
        return int(root + 0.5) ** 2 == integer

    if not is_square(1 + 8 * a_00) or not is_square(1 + 8 * a_11):
        return 'Impossible'

    z = 1 + math.sqrt(1 + 8 * a_00)
    o = 1 + math.sqrt(1 + 8 * a_11)

    if z % 2 == 1 or o % 2 == 1:
        return 'Impossible'

    z = int(z / 2)
    o = int(o / 2)

    if a_00 == 0 and a_01 == 0 and a_10 == 0:
        z = 0
    if a_11 == 0 and a_01 == 0 and a_10 == 0:
        o = 0

    if z * o != a_01 + a_10:
        return 'Impossible'

    if z == 0 and o == 0:
        return '0'

    s = z * o
    ans = []

    while True:
        if s - z >= a_01:
            ans.append('1')
            s -= z
            o -= 1
        else:
            ans.append('0')
            z -= 1
        if z == 0 and o == 0:
            break

    return ''.join(ans)