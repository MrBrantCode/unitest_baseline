"""
QUESTION:
There are N people (with different names) and K clubs. For each club you know the list of members (so you have K unordered lists). Each person can be a member of many clubs (and also 0 clubs) and two different clubs might have exactly the same members. The value of the number K is the minimum possible such that the following property can be true for at least one configuration of clubs. If every person changes her name (maintaining the property that all names are different) and you know the new K lists of members of the clubs (but you don't know which list corresponds to which club), you are sure that you would be able to match the old names with the new ones.

Count the number of such configurations of clubs (or say that there are more than 1000). Two configurations of clubs that can be obtained one from the other if the N people change their names are considered equal.

Formal statement: A club is a (possibly empty) subset of \\{1,\dots, N\\} (the subset identifies the members, assuming that the people are indexed by the numbers 1, 2,\dots, N). A configuration of clubs is an unordered collection of K clubs (not necessarily distinct). Given a permutation \sigma(1), \dots, \sigma(N) of \\{1,\dots, N\\} and a configuration of clubs L=\\{C_1, C_2, \dots, C_K\\}, we denote with \sigma(L) the configuration of clubs \\{\sigma(C_1), \sigma(C_2), \dots, \sigma(C_K)\\} (if C is a club, \sigma(C)=\\{\sigma(x):\, x\in C\\}). A configuration of clubs L is name-preserving if for any pair of distinct permutations \sigma\not=\tau, it holds \sigma(L)\not=\tau(L).

You have to count the number of name-preserving configurations of clubs with the minimum possible number of clubs (so K is minimum). Two configurations L_1, L_2 such that L_2=\sigma(L_1) (for some permutation \sigma) are considered equal. If there are more than 1000 such configurations, print -1.

Constraints

* 2 \le N \le 2\cdot10^{18}

Input

The input is given from Standard Input in the format


N


Output

If ans is the number of configurations with the properties described in the statement, you should print on Standard Output


ans


If there are more than 1000 such configurations, print -1.

Examples

Input

2


Output

1


Input

3


Output

1


Input

4


Output

7


Input

13


Output

6


Input

26


Output

-1


Input

123456789123456789


Output

-1
"""

def count_name_preserving_configurations(N):
    # Dictionary mapping N to the number of name-preserving configurations
    dic = {
        1: 1, 2: 1, 3: 1, 4: 7, 5: 4, 6: 1, 7: 336, 8: 384, 9: 334, 10: 220, 11: 108, 12: 36, 13: 6,
        27: 976, 28: 108, 29: 4, 60: 220, 61: 1, 124: 334, 252: 384, 508: 334, 1020: 220, 2044: 108,
        4092: 36, 8188: 6, 134217723: 976, 268435451: 108, 536870907: 4, 1152921504606846970: 220,
        2305843009213693946: 1
    }
    
    # Check if N is in the dictionary
    if N in dic:
        return dic[N]
    else:
        return -1