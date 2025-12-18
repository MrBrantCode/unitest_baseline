"""
QUESTION:
Implement a function `pourWater(heights, V, K, obstacles)` that simulates pouring `V` units of water onto a terrain represented by the `heights` list at position `K`, considering the presence of obstacles at positions specified in the `obstacles` list. The function should return the updated `heights` list after pouring all the water. The water should be poured according to the following rules: 

1. Water can only be poured to the left or right if the height at the current position is greater than or equal to the height of the adjacent position.
2. If pouring water at the current position would cause it to flow to the adjacent position, the water should be poured at the current position instead.
3. If pouring water to the left or right is not possible, pour the water at the current position `K`.

Restrictions: The input lists `heights` and `obstacles` are non-empty and contain non-negative integers. The value `V` is a non-negative integer, and `K` is a valid index within the `heights` list.
"""

def pourWater(heights, V, K, obstacles):
    while V > 0:
        l = r = K
        # While water can still drop to the left, drop the water to the left
        while l > 0 and heights[l] >= heights[l - 1] and l not in obstacles:
            l -= 1
        # While water can still drop to the right, drop the water to the right
        while r < len(heights) - 1 and heights[r] >= heights[r + 1] and r not in obstacles:
            r += 1
        # Drop the water to the left if doing so doesn't cause it to flow to the right
        if l and heights[l] < heights[l + 1] and heights[l] <= heights[K] and l not in obstacles:
            heights[l] += 1
        # Drop the water to the right if doing so doesn't cause it to flow to the left
        elif r < len(heights) - 1 and heights[r] <= heights[r + 1] and heights[r] <= heights[K] and r not in obstacles:
            heights[r] += 1
        # Drop the water at K
        else:
            heights[K] += 1
        V -= 1
    return heights