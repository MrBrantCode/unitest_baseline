"""
QUESTION:
You are given two integers b and w. You have a chessboard of size 10^9 × 10^9 with the top left cell at (1; 1), the cell (1; 1) is painted white.

Your task is to find a connected component on this chessboard that contains exactly b black cells and exactly w white cells. Two cells are called connected if they share a side (i.e. for the cell (x, y) there are at most four connected cells: (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)). A set of cells is called a connected component if for every pair of cells C_1 and C_2 from this set, there exists a sequence of cells c_1, c_2, ..., c_k such that c_1 = C_1, c_k = C_2, all c_i from 1 to k are belong to this set of cells and for every i ∈ [1, k - 1], cells c_i and c_{i + 1} are connected.

Obviously, it can be impossible to find such component. In this case print "NO". Otherwise, print "YES" and any suitable connected component.

You have to answer q independent queries.

Input

The first line of the input contains one integer q (1 ≤ q ≤ 10^5) — the number of queries. Then q queries follow.

The only line of the query contains two integers b and w (1 ≤ b, w ≤ 10^5) — the number of black cells required and the number of white cells required.

It is guaranteed that the sum of numbers of cells does not exceed 2 ⋅ 10^5 (∑ w + ∑ b ≤ 2 ⋅ 10^5).

Output

For each query, print the answer to it.

If it is impossible to find the required component, print "NO" on the first line.

Otherwise, print "YES" on the first line. In the next b + w lines print coordinates of cells of your component in any order. There should be exactly b black cells and w white cells in your answer. The printed component should be connected.

If there are several answers, you can print any. All coordinates in the answer should be in the range [1; 10^9].

Example

Input


3
1 1
1 4
2 5


Output


YES
2 2
1 2
YES
2 3
1 3
3 3
2 2
2 4
YES
2 3
2 4
2 5
1 3
1 5
3 3
3 5
"""

def find_connected_component(b, w):
    maxi, mini = max(b, w), min(b, w)
    points = []
    
    if maxi <= mini * 3 + 1:
        result = "YES"
        if w > b:
            z = 0
        else:
            z = 1
        
        for i in range(2 * mini):
            points.append((2 + i + z, 2))
        
        rem = maxi - mini
        if rem != 0:
            points.append((3 + z + i, 2))
            rem -= 1
        
        for j in range(3 + z, 3 + i + z + 1, 2):
            if rem > 0:
                points.append((j, 1))
                rem -= 1
            if rem > 0:
                points.append((j, 3))
                rem -= 1
    else:
        result = "NO"
        points = []
    
    return result, points