"""
QUESTION:
Write a function named `maxDistance` that takes three inputs: a list of integers `position` representing the positions of `n` empty baskets, an integer `m` representing the number of balls, and a list of integers `obstacle` representing the positions of obstacles. The function should return the maximum minimum magnetic force between any two balls after distributing the balls into the baskets. 

The magnetic force between two different balls at positions `x` and `y` is `|x - y|`. The positions in `position` and `obstacle` are distinct and within the range [1, 10^9]. The length of `position` is within the range [2, 10^5] and the length of `obstacle` is within the range [0, 10^5]. The number of balls `m` is within the range [2, n].
"""

def maxDistance(position, m, obstacle):
    n = len(position)
    position.sort()
    obs_set = set(obstacle)
    l, r = 0, position[-1] - position[0] + 1

    def check(gap):
        cur = position[0]
        cnt = 1
        for i in range(1, len(position)):
            if position[i] < cur + gap or position[i] in obs_set:
                continue
            cur = position[i]
            cnt += 1
            if cnt == m:
                return True
        return False

    while l < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid + 1
        else:
            r = mid
    return l - 1