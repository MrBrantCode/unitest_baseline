"""
QUESTION:
In a kindergarten, the children are being divided into groups. The teacher put the children in a line and associated each child with his or her integer charisma value. Each child should go to exactly one group. Each group should be a nonempty segment of consecutive children of a line. A group's sociability is the maximum difference of charisma of two children in the group (in particular, if the group consists of one child, its sociability equals a zero). 

The teacher wants to divide the children into some number of groups in such way that the total sociability of the groups is maximum. Help him find this value.

Input

The first line contains integer n — the number of children in the line (1 ≤ n ≤ 106).

The second line contains n integers ai — the charisma of the i-th child ( - 109 ≤ ai ≤ 109).

Output

Print the maximum possible total sociability of all groups.

Examples

Input

5
1 2 3 1 2


Output

3


Input

3
3 3 3


Output

0

Note

In the first test sample one of the possible variants of an division is following: the first three children form a group with sociability 2, and the two remaining children form a group with sociability 1.

In the second test sample any division leads to the same result, the sociability will be equal to 0 in each group.
"""

def calculate_maximum_sociability(n, charisma_values):
    dp = [0] * n
    pos, neg = -10**18, -10**18
    
    for i, x in enumerate(charisma_values):
        prv = 0 if i == 0 else dp[i - 1]
        dp[i] = max(neg + x, pos - x, prv)
        pos = max(pos, prv + x)
        neg = max(neg, prv - x)
    
    return dp[-1]