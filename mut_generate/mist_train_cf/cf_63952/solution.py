"""
QUESTION:
Implement the function `pourWater(heights, V, K, obstacles)` where `heights` is a list of integers representing the height of the terrain at each index, `V` is an integer representing the volume of water, `K` is an integer representing the index where the water falls, and `obstacles` is a list of indices representing the positions of obstacles. The function should return a list of integers representing the height of the terrain at each index after the water has fallen and flowed according to the rules. 

The water flows according to the following rules: 
- If the droplet would eventually fall by moving left, then move left.
- Otherwise, if the droplet would eventually fall by moving right, then move right.
- Otherwise, rise at its current position.
The height of the terrain plus any water in that column is referred to as the "level". 

Constraints: 
- `heights` will have length in `[1, 100]` and contain integers in `[0, 99]`.
- `V` will be in range `[0, 2000]`.
- `K` will be in range `[0, heights.length - 1]`.
- `obstacles` will be a list of indices in `heights` and will not include `K`.
"""

def pourWater(heights, V, K, obstacles):
    while V > 0:
        l = r = K
        while l > 0 and heights[l] >= heights[l - 1] and l-1 not in obstacles:
            l -= 1
        while r < len(heights) - 1 and heights[r] >= heights[r + 1] and r+1 not in obstacles:
            r += 1
        if l and heights[l] < heights[l + 1] and heights[l] <= heights[K] and l not in obstacles:
            heights[l] += 1
        elif r < len(heights) - 1 and heights[r] < heights[r - 1] and heights[r] <= heights[K] and r not in obstacles:
            heights[r] += 1
        else:
            heights[K] += 1
        V -= 1
    return heights