"""
QUESTION:
You are given $n$ segments on a coordinate axis $OX$. The $i$-th segment has borders $[l_i; r_i]$. All points $x$, for which $l_i \le x \le r_i$ holds, belong to the $i$-th segment.

Your task is to choose the maximum by size (the number of segments) subset of the given set of segments such that each pair of segments in this subset either non-intersecting or one of them lies inside the other one.

Two segments $[l_i; r_i]$ and $[l_j; r_j]$ are non-intersecting if they have no common points. For example, segments $[1; 2]$ and $[3; 4]$, $[1; 3]$ and $[5; 5]$ are non-intersecting, while segments $[1; 2]$ and $[2; 3]$, $[1; 2]$ and $[2; 2]$ are intersecting.

The segment $[l_i; r_i]$ lies inside the segment $[l_j; r_j]$ if $l_j \le l_i$ and $r_i \le r_j$. For example, segments $[2; 2]$, $[2, 3]$, $[3; 4]$ and $[2; 4]$ lie inside the segment $[2; 4]$, while $[2; 5]$ and $[1; 4]$ are not.

You have to answer $t$ independent test cases.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases. Then $t$ test cases follow.

The first line of the test case contains one integer $n$ ($1 \le n \le 3000$) — the number of segments. The next $n$ lines describe segments. The $i$-th segment is given as two integers $l_i$ and $r_i$ ($1 \le l_i \le r_i \le 2 \cdot 10^5$), where $l_i$ is the left border of the $i$-th segment and $r_i$ is the right border of the $i$-th segment.

Additional constraint on the input: there are no duplicates in the list of segments.

It is guaranteed that the sum of $n$ does not exceed $3000$ ($\sum n \le 3000$).


-----Output-----

For each test case, print the answer: the maximum possible size of the subset of the given set of segments such that each pair of segments in this subset either non-intersecting or one of them lies inside the other one.


-----Example-----
Input
4
4
1 5
2 4
2 3
3 4
5
1 5
2 3
2 5
3 5
2 2
3
1 3
2 4
2 3
7
1 10
2 8
2 5
3 4
4 4
6 8
7 7

Output
3
4
2
7
"""

def max_subset_size(test_cases):
    results = []
    
    for case in test_cases:
        n = len(case)
        pointList = []
        pointOrderDict = {}
        interval = case
        intervalOrder = []
        
        for l, r in interval:
            pointList.append(l)
            pointList.append(r)
        
        pointList.sort()
        cnt = 0
        
        for i in range(2 * n):
            if i == 0 or pointList[i] != pointList[i - 1]:
                pointOrderDict[pointList[i]] = cnt
                cnt += 1
        
        for elem in interval:
            intervalOrder.append((pointOrderDict[elem[0]], pointOrderDict[elem[1]]))
        
        intervalList = []
        dp = []
        
        for i in range(cnt):
            dp.append([])
            intervalList.append([])
            for j in range(cnt):
                dp[i].append(-1)
        
        for elem in intervalOrder:
            intervalList[elem[0]].append(elem[1])
        
        for i in range(cnt):
            for j in range(cnt - i):
                ans1 = 0
                ans2 = 0
                if i != 0:
                    ans2 = dp[j + 1][i + j]
                for elem in intervalList[j]:
                    if elem == i + j:
                        ans1 += 1
                    elif elem < i + j and ans2 < dp[j][elem] + dp[elem + 1][i + j]:
                        ans2 = dp[j][elem] + dp[elem + 1][i + j]
                dp[j][i + j] = ans1 + ans2
        
        results.append(dp[0][cnt - 1])
    
    return results