"""
QUESTION:
Write a function `maxArea` that takes the height `h`, width `w`, arrays of integers `horizontalCuts` and `verticalCuts`, and array of pairs `obstacles` as input, where `obstacles[i]` is an array of three integers representing the row, column, and radius of the `i-th` obstacle. The function should return the maximum area of a piece of cake after cutting at each horizontal and vertical position provided in the arrays `horizontalCuts` and `verticalCuts` without cutting through any obstacles or within the radius of any obstacle, modulo `10^9 + 7`. The function should follow these constraints:
- `2 <= h, w < 10^9`
- `1 <= horizontalCuts.length <= min(h, 10^5)`
- `1 <= verticalCuts.length <= min(w, 10^5)`
- `1 <= horizontalCuts[i] < h`
- `1 <= verticalCuts[i] < w`
- `0 <= obstacles.length <= min(h*w, 10^5)`
- `1 <= obstacles[i][0] <= h`
- `1 <= obstacles[i][1] <= w`
- `0 <= obstacles[i][2] <= min(h, w)`
- All elements in `horizontalCuts`, `verticalCuts`, and `obstacles` are distinct.
"""

def maxArea(h, w, horizontalCuts, verticalCuts, obstacles):
    MOD = 10**9 + 7
    def maxGap(cuts, n):
        cuts.sort()
        max_val = max(cuts[0], n - cuts[-1])
        for i in range(1, len(cuts)):
            max_val = max(max_val, cuts[i] - cuts[i-1])
        return max_val
    
    # Check if any obstacle intercepts any cut
    def is_valid(x, y, r, cut):
        return abs(x - cut) > r

    # Filter out horizontal cuts
    h_cuts = [0] + [hc for hc in horizontalCuts if all(is_valid(ob[1], ob[0], ob[2], hc) for ob in obstacles)] + [h]
    # Filter out vertical cuts
    v_cuts = [0] + [vc for vc in verticalCuts if all(is_valid(ob[0], ob[1], ob[2], vc) for ob in obstacles)] + [w]
    
    # Calculate maxH and maxV
    maxH = maxGap(h_cuts, h)
    maxV = maxGap(v_cuts, w)
    
    return (maxH * maxV) % MOD