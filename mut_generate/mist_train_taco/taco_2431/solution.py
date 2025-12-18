"""
QUESTION:
Evlampiy has found one more cool application to process photos. However the application has certain limitations.

Each photo i has a contrast v_{i}. In order for the processing to be truly of high quality, the application must receive at least k photos with contrasts which differ as little as possible.

Evlampiy already knows the contrast v_{i} for each of his n photos. Now he wants to split the photos into groups, so that each group contains at least k photos. As a result, each photo must belong to exactly one group.

He considers a processing time of the j-th group to be the difference between the maximum and minimum values of v_{i} in the group. Because of multithreading the processing time of a division into groups is the maximum processing time among all groups.

Split n photos into groups in a such way that the processing time of the division is the minimum possible, i.e. that the the maximum processing time over all groups as least as possible.


-----Input-----

The first line contains two integers n and k (1 ≤ k ≤ n ≤ 3·10^5) — number of photos and minimum size of a group.

The second line contains n integers v_1, v_2, ..., v_{n} (1 ≤ v_{i} ≤ 10^9), where v_{i} is the contrast of the i-th photo.


-----Output-----

Print the minimal processing time of the division into groups.


-----Examples-----
Input
5 2
50 110 130 40 120

Output
20

Input
4 1
2 3 4 1

Output
0



-----Note-----

In the first example the photos should be split into 2 groups: [40, 50] and [110, 120, 130]. The processing time of the first group is 10, and the processing time of the second group is 20. Maximum among 10 and 20 is 20. It is impossible to split the photos into groups in a such way that the processing time of division is less than 20.

In the second example the photos should be split into four groups, each containing one photo. So the minimal possible processing time of a division is 0.
"""

def minimal_processing_time(n, k, v):
    def f(m):
        nonlocal dp, sdp
        l = 0
        for i in range(n):
            while l < n and v[l] < v[i] - m:
                l += 1
            if l - 1 > i - k:
                dp[i] = False
            else:
                dp[i] = sdp[i - k + 1] != sdp[l - 1]
            sdp[i + 1] = sdp[i] + (1 if dp[i] else 0)
        return dp[n - 1]

    dp = [False for _ in range(n + 2)]
    sdp = [0 for _ in range(n + 2)]
    dp[-1] = True
    sdp[0] = 1
    v.sort()
    le = -1
    r = v[-1] - v[0]
    while r - le > 1:
        m = (r + le) // 2
        if f(m):
            r = m
        else:
            le = m
    return r