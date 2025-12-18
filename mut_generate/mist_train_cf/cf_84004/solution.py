"""
QUESTION:
Given `n` cuboids with dimensions `cuboids[i] = [widthi, lengthi, heighti]`, determine the maximum possible height that can be achieved by stacking a subset of these cuboids. The stacking rule is that cuboid `i` can be placed on cuboid `j` if `widthi <= widthj`, `lengthi <= lengthj`, and `heighti <= heightj`, with the option to rotate any cuboid to fit on another. The dimensions are all between 1 and 100, and there are between 1 and 100 cuboids. The function to solve this problem is `maxHeight(cuboids)`.
"""

def maxHeight(cuboids):
    for cuboid in cuboids:
        cuboid.sort()

    cuboids.sort(reverse=True)
    dp = [0] * len(cuboids)
    for i in range(len(cuboids)):
        dp[i] = cuboids[i][2]
        for j in range(i):
            if cuboids[i][0]<=cuboids[j][0] and cuboids[i][1]<=cuboids[j][1] and cuboids[i][2]<=cuboids[j][2]:
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])

    return max(dp)