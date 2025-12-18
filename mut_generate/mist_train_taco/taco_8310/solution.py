"""
QUESTION:
We have a board with a 2 \times N grid.
Snuke covered the board with N dominoes without overlaps.
Here, a domino can cover a 1 \times 2 or 2 \times 1 square.
Then, Snuke decided to paint these dominoes using three colors: red, cyan and green.
Two dominoes that are adjacent by side should be painted by different colors.
Here, it is not always necessary to use all three colors.
Find the number of such ways to paint the dominoes, modulo 1000000007.
The arrangement of the dominoes is given to you as two strings S_1 and S_2 in the following manner:
 - Each domino is represented by a different English letter (lowercase or uppercase).
 - The j-th character in S_i represents the domino that occupies the square at the i-th row from the top and j-th column from the left.

-----Constraints-----
 - 1 \leq N \leq 52
 - |S_1| = |S_2| = N
 - S_1 and S_2 consist of lowercase and uppercase English letters.
 - S_1 and S_2 represent a valid arrangement of dominoes.

-----Input-----
Input is given from Standard Input in the following format:
N
S_1
S_2

-----Output-----
Print the number of such ways to paint the dominoes, modulo 1000000007.

-----Sample Input-----
3
aab
ccb

-----Sample Output-----
6

There are six ways as shown below:
"""

def count_painting_ways(N, S1, S2):
    mod = 10**9 + 7
    l = ''
    
    # Determine the type of each domino (vertical or horizontal)
    for i in range(N):
        if S1[i] == S2[i]:
            l += 'X'  # Vertical domino
        else:
            l += 'Y'  # Horizontal domino
    
    # Collapse consecutive 'Y's into a single 'Y'
    l = l.replace('YY', 'Y')
    
    # Initialize the answer based on the first domino
    ans = 6 if l[0] == 'Y' else 3
    
    # Calculate the number of ways to paint the dominoes
    for i in range(1, len(l)):
        if l[i] == 'Y' and l[i - 1] == 'Y':
            ans *= 3
        elif l[i] == 'X' and l[i - 1] == 'X':
            ans *= 2
        elif l[i] == 'Y' and l[i - 1] == 'X':
            ans *= 2
        ans = ans % mod
    
    return ans