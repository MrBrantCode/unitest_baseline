"""
QUESTION:
As of now, you helped agent OO7 to find men with different capability values. Now his task is to group up his men and work as a team. He wants to form the groups with minimum 2 men in it. Help him out to find how many such groups are possible.
Input - First line contains 'T' test cases followed by 'T' lines containing number of men, ‘N’.
Output - 'T' lines containing total number of possible groups.
Constraints - 1 ≤ T ≤ 10^3 ,  1 ≤ N ≤ 200

SAMPLE INPUT
2
4
6

SAMPLE OUTPUT
2
4

Explanation

1) For the 1st case, N is 4. Possible group size can be {2,2}, {4}. So, output is 2.
2) For the 2nd case, N is 6. Possible group size can be {2,2,2}, {2,4}, {3,3}, {6}. So, output is 4.
"""

def calculate_possible_groups(N):
    groupSize = dict()

    def gs(n, m):
        if m < 2:
            return 0
        if m == n:
            return 1
        if n < m:
            return 0
        if (n, m) in groupSize:
            return groupSize[(n, m)]
        res = 1
        for i in range(m, n):
            res += gs(n - i, i)
        groupSize[(n, m)] = res
        return res

    return gs(N, 2)