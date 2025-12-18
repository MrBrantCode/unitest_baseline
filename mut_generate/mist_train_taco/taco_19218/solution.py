"""
QUESTION:
It’s well know fact among kitties that digits 4 and 7 are lucky digits.
Today, N boxes of fish bites arrived. Each box has a unique integer label on it, ranged between 1 and N, inclusive. The boxes are going to be given away to the kitties in increasing order of their labels. That is, the first box given away will be the box with label 1, and the last one will be the box with label N.

The kitties are ordered in line for the fish bites. While there is any fish bites box left, it’s given away to the cat who is the first in line for it. This cat counts the total number of lucky digits among all box labels received by him. As soon as this number exceeds K, the cat becomes lucky and leaves the line, and the next cat occupies his place.

Your task is to find out the number of kitties that are going to be lucky at the end of the described process.

Input format

The first line of the input contains the integer K. The second line contains the integer N, without leading zeros.

Output format

In the only line of the output print the number of lucky kitties modulo 1,000,000,007.

Constraints

N is between 1 and 10^10000 and K is between 1 and 10, inclusive.

SAMPLE INPUT
3
74

SAMPLE OUTPUT
7
"""

def count_lucky_kitties(k: int, n: str) -> int:
    MOD = 1_000_000_007
    a = 0  # Count of '4' digits
    b = 0  # Count of '7' digits
    cnt = 0  # Count of lucky kitties
    
    for i in range(1, int(n) + 1):
        a += str(i).count('4')
        b += str(i).count('7')
        if a + b > k:
            cnt += 1
            a = 0
            b = 0
    
    return cnt % MOD