"""
QUESTION:
There are N points on a number line, i-th of which is placed on coordinate X_i. These points are numbered in the increasing order of coordinates. In other words, for all i (1 \leq i \leq N-1), X_i < X_{i+1} holds. In addition to that, an integer K is given.

Process Q queries.

In the i-th query, two integers L_i and R_i are given. Here, a set s of points is said to be a good set if it satisfies all of the following conditions. Note that the definition of good sets varies over queries.

* Each point in s is one of X_{L_i},X_{L_i+1},\ldots,X_{R_i}.
* For any two distinct points in s, the distance between them is greater than or equal to K.
* The size of s is maximum among all sets that satisfy the aforementioned conditions.



For each query, find the size of the union of all good sets.

Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq K \leq 10^9
* 0 \leq X_1 < X_2 < \cdots < X_N \leq 10^9
* 1 \leq Q \leq 2 \times 10^5
* 1 \leq L_i \leq R_i \leq N
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N K
X_1 X_2 \cdots X_N
Q
L_1 R_1
L_2 R_2
\vdots
L_Q R_Q


Output

For each query, print the size of the union of all good sets in a line.

Examples

Input

5 3
1 2 4 7 8
2
1 5
1 2


Output

4
2


Input

15 220492538
4452279 12864090 23146757 31318558 133073771 141315707 263239555 350278176 401243954 418305779 450172439 560311491 625900495 626194585 891960194
5
6 14
1 8
1 13
7 12
4 12


Output

4
6
11
2
3
"""

def find_good_sets_size(n, k, points, queries):
    L = 18
    xid = [0] * (n * L)
    xsum = [0] * (n * L)
    yid = [0] * (n * L)
    ysum = [0] * (n * L)
    
    # Preprocess xid and xsum
    j = n
    for i in reversed(range(n)):
        while i < j and points[i] + k <= points[j - 1]:
            j -= 1
        xid[i * L + 0] = j
        xsum[i * L + 0] = j
        for lv in range(1, L):
            a = xid[i * L + lv - 1]
            if a == n:
                xid[i * L + lv] = n
            else:
                xid[i * L + lv] = xid[a * L + lv - 1]
                xsum[i * L + lv] = xsum[i * L + lv - 1] + xsum[a * L + lv - 1]
    
    # Preprocess yid and ysum
    j = -1
    for i in range(n):
        while j < i and points[j + 1] + k <= points[i]:
            j += 1
        yid[i * L + 0] = j
        ysum[i * L + 0] = j
        for lv in range(1, L):
            a = yid[i * L + lv - 1]
            if a == -1:
                yid[i * L + lv] = -1
            else:
                yid[i * L + lv] = yid[a * L + lv - 1]
                ysum[i * L + lv] = ysum[i * L + lv - 1] + ysum[a * L + lv - 1]
    
    # Process each query
    results = []
    for (l, r) in queries:
        l -= 1
        r -= 1
        ans = 0
        i = l
        ans -= i
        for lv in reversed(range(L)):
            if xid[i * L + lv] <= r:
                ans -= xsum[i * L + lv]
                i = xid[i * L + lv]
        i = r
        ans += i + 1
        for lv in reversed(range(L)):
            if yid[i * L + lv] >= l:
                ans += ysum[i * L + lv] + (1 << lv)
                i = yid[i * L + lv]
        results.append(ans)
    
    return results