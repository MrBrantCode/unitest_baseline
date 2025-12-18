"""
QUESTION:
problem

One day, Taro, who lives in JOI town, decided to take a walk as a daily routine to improve his health. In JOI town, where Taro lives, he runs in the east-west direction as shown in the figure (H + 1). The road and the north-south direction (W + 1) run through the road in a grid pattern. Taro's house is at the northwestern intersection, and the walk starts from here.

Hereafter, the ath intersection from the north and the bth intersection from the west are represented by (a, b). For example, the intersection where Taro's house is located is (1, 1).


<image>

Figure: JOI town map (for H = 3, W = 4). The top of the figure corresponds to the north and the left corresponds to the west.

Taro thought that it would be more interesting if the walking route was different every day, so he wrote the letters "east" or "south" at the H x W intersections from (1, 1) to (H, W). , I decided to take a walk every day according to the following rules.

* If you are at an intersection with letters, rewrite the letters from "east" to "south" and "south" to "east", and the direction of the originally written letters. Proceed to the next intersection at.
* End the walk when you reach the easternmost or southernmost road.



After thinking about this plan, Taro was wondering what route he would take in his future walks. For Taro, he predicted the route for Taro's Nth walk. Create a program to do.



input

The input consists of multiple datasets. Each dataset is given in the following format.

On the first line, three positive integers are separated by blanks. These are the values ​​of the three numbers H, W, N in the problem statement. H, W, N are 1 ≤ H ≤, respectively. 1000, 1 ≤ W ≤ 1000, 1 ≤ N ≤ 10000000 = 107. From the 2nd line to H + 1st line, W integers are written separated by blanks. Represents the information of the character written at the intersection first. If the jth integer of i + 1st line is 0, the character written at the intersection (i, j) is "south", and if it is 1, the intersection Indicates that the character written in (i, j) is "east".

Of the scoring data, 30% of the points are satisfied with H ≤ 100, W ≤ 100, and N ≤ 1000.

When H, W, N are all 0, it indicates the end of input. The number of data sets does not exceed 10.

output

Output in the following format for each data set.
When the intersection where Taro finishes the walk in the Nth walk is (i, j), output i and j separated by a blank in this order.

Example

Input

3 4 3
1 0 1 1
0 1 0 0
1 0 1 0
0 0 0


Output

1 5
"""

def find_taro_walk_destination(h, w, n, grid):
    # Initialize the dp array with zeros
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = n - 1
    
    # Fill the dp array based on the grid and initial walk count
    for i in range(h):
        for j in range(w):
            if i < h - 1 and grid[i][j] == 0:
                dp[i + 1][j] += (dp[i][j] + 1) // 2
            if i < h - 1 and grid[i][j] == 1:
                dp[i + 1][j] += dp[i][j] // 2
            if j < w - 1 and grid[i][j] == 0:
                dp[i][j + 1] += dp[i][j] // 2
            if j < w - 1 and grid[i][j] == 1:
                dp[i][j + 1] += (dp[i][j] + 1) // 2
    
    # Update the grid based on the dp array
    for i in range(h):
        for j in range(w):
            grid[i][j] = (grid[i][j] + dp[i][j]) % 2
    
    # Determine the final position after the walk
    i, j = 0, 0
    while i < h and j < w:
        if grid[i][j] == 0:
            i += 1
        else:
            j += 1
    
    # Return the 1-based index of the final position
    return (i + 1, j + 1)