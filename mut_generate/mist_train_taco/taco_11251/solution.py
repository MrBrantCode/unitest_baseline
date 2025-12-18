"""
QUESTION:
Let S be the concatenation of 10^{10} copies of the string 110. (For reference, the concatenation of 3 copies of 110 is 110110110.)
We have a string T of length N.
Find the number of times T occurs in S as a contiguous substring.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - T is a string of length N consisting of 0 and 1.

-----Input-----
Input is given from Standard Input in the following format:
N
T

-----Output-----
Print the number of times T occurs in S as a contiguous substring.

-----Sample Input-----
4
1011

-----Sample Output-----
9999999999

S is so long, so let us instead count the number of times 1011 occurs in the concatenation of 3 copies of 110, that is, 110110110. We can see it occurs twice:
 - 1 1011 0110
 - 1101 1011 0
"""

def count_occurrences_in_infinite_string(N: int, T: str) -> int:
    if N == 1:
        if T == '0':
            return 10 ** 10
        else:
            return 2 * 10 ** 10
    elif N == 2:
        if T == '00':
            return 0
        elif T == '01':
            return 10 ** 10 - 1
        elif T == '10':
            return 10 ** 10
        else:
            return 10 ** 10
    else:
        repeat_num = (N + 6) // 3
        ref = '110' * repeat_num
        num_in_ref = 0
        flag_over = 0
        if ref[:N] == T:
            num_in_ref += 1
            if N % 3 == 0:
                flag_over = 1
        elif ref[1:N + 1] == T:
            num_in_ref += 1
        elif ref[2:N + 2] == T:
            num_in_ref += 1
            if N % 3 == 2:
                flag_over = -1
        return num_in_ref * (10 ** 10 - repeat_num + 2) + flag_over