"""
QUESTION:
[THE SxPLAY & KIVΛ - 漂流](https://soundcloud.com/kivawu/hyouryu)

[KIVΛ & Nikki Simmons - Perspectives](https://soundcloud.com/kivawu/perspectives)

With a new body, our idol Aroma White (or should we call her Kaori Minamiya?) begins to uncover her lost past through the OS space.

The space can be considered a 2D plane, with an infinite number of data nodes, indexed from 0, with their coordinates defined as follows:

  * The coordinates of the 0-th node is (x_0, y_0) 
  * For i > 0, the coordinates of i-th node is (a_x ⋅ x_{i-1} + b_x, a_y ⋅ y_{i-1} + b_y) 



Initially Aroma stands at the point (x_s, y_s). She can stay in OS space for at most t seconds, because after this time she has to warp back to the real world. She doesn't need to return to the entry point (x_s, y_s) to warp home.

While within the OS space, Aroma can do the following actions:

  * From the point (x, y), Aroma can move to one of the following points: (x-1, y), (x+1, y), (x, y-1) or (x, y+1). This action requires 1 second. 
  * If there is a data node at where Aroma is staying, she can collect it. We can assume this action costs 0 seconds. Of course, each data node can be collected at most once. 



Aroma wants to collect as many data as possible before warping back. Can you help her in calculating the maximum number of data nodes she could collect within t seconds?

Input

The first line contains integers x_0, y_0, a_x, a_y, b_x, b_y (1 ≤ x_0, y_0 ≤ 10^{16}, 2 ≤ a_x, a_y ≤ 100, 0 ≤ b_x, b_y ≤ 10^{16}), which define the coordinates of the data nodes.

The second line contains integers x_s, y_s, t (1 ≤ x_s, y_s, t ≤ 10^{16}) – the initial Aroma's coordinates and the amount of time available.

Output

Print a single integer — the maximum number of data nodes Aroma can collect within t seconds.

Examples

Input


1 1 2 3 1 0
2 4 20


Output


3

Input


1 1 2 3 1 0
15 27 26


Output


2

Input


1 1 2 3 1 0
2 2 1


Output


0

Note

In all three examples, the coordinates of the first 5 data nodes are (1, 1), (3, 3), (7, 9), (15, 27) and (31, 81) (remember that nodes are numbered from 0).

In the first example, the optimal route to collect 3 nodes is as follows: 

  * Go to the coordinates (3, 3) and collect the 1-st node. This takes |3 - 2| + |3 - 4| = 2 seconds. 
  * Go to the coordinates (1, 1) and collect the 0-th node. This takes |1 - 3| + |1 - 3| = 4 seconds. 
  * Go to the coordinates (7, 9) and collect the 2-nd node. This takes |7 - 1| + |9 - 1| = 14 seconds. 



In the second example, the optimal route to collect 2 nodes is as follows: 

  * Collect the 3-rd node. This requires no seconds. 
  * Go to the coordinates (7, 9) and collect the 2-th node. This takes |15 - 7| + |27 - 9| = 26 seconds. 



In the third example, Aroma can't collect any nodes. She should have taken proper rest instead of rushing into the OS space like that.
"""

def max_data_nodes_collected(x0, y0, ax, ay, bx, by, xs, ys, t):
    def abs(x):
        return 0 - x if x < 0 else x

    def max(x, y):
        return x if x > y else y

    def dfs(idx, left, currx, curry, dir, cnt):
        nonlocal maxx, arr
        if dir == 0:
            if idx < 0:
                maxx = max(maxx, cnt)
                return
            elif abs(currx - arr[idx][0]) + abs(curry - arr[idx][1]) <= left:
                dfs(idx - 1, left - (abs(currx - arr[idx][0]) + abs(curry - arr[idx][1])), arr[idx][0], arr[idx][1], 0, cnt + 1)
            else:
                maxx = max(maxx, cnt)
        elif idx >= len(arr):
            maxx = max(maxx, cnt)
            return
        elif abs(currx - arr[idx][0]) + abs(curry - arr[idx][1]) <= left:
            dfs(idx + 1, left - (abs(currx - arr[idx][0]) + abs(curry - arr[idx][1])), arr[idx][0], arr[idx][1], 1, cnt + 1)
        else:
            maxx = max(maxx, cnt)

    arr = [[x0, y0]]
    maxx = 0
    currx = x0
    curry = y0
    
    # Generate the coordinates of the data nodes
    for _ in range(100):
        currx = ax * currx + bx
        curry = ay * curry + by
        arr.append([currx, curry])
    
    # Perform DFS to find the maximum number of data nodes that can be collected
    for i in range(100):
        dfs(i, t, xs, ys, 0, 0)
        dfs(i, t, xs, ys, 1, 0)
    
    return maxx