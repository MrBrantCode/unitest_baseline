"""
QUESTION:
k kids seem to have visited your home for the festival. It seems like the kids
had all been fighting with each other, so you decided to keep them as far as
possible from each other. You had placed n chairs on the positive number line,
each at position x i , 1 ≤ i ≤ n. You can make the kids sit in any of the chairs.
Now you want to know the largest possible minimum distance between each kid.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains two lines. First line contains two space separated integers n and k. Second line contains n space separated values, x1, x2, x3, … ,xn.

-----Output:-----
For each test case print the largest possible minimum distance.

-----Sample Input:-----
1

2 2

1 2    

-----Sample Output:-----
1  

-----Constraints-----
- $2 \leq n \leq 100000$
- $0 \leq xi \leq 10^9$
- $k \leq n $
"""

def largest_min_distance(n, k, positions):
    def check(mid):
        pos = positions[0]
        ct = 1
        for i in range(1, n):
            if positions[i] - pos >= mid:
                pos = positions[i]
                ct += 1
                if ct == k:
                    return True
        return False

    positions.sort()
    ans = -1
    l, r = 1, positions[-1]
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            ans = max(ans, mid)
            l = mid + 1
        else:
            r = mid
    return ans