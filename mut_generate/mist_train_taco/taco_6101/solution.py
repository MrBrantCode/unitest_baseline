"""
QUESTION:
You are given a marine area map that is a mesh of squares, each representing either a land or sea area. Figure B-1 is an example of a map.

<image>
Figure B-1: A marine area map

You can walk from a square land area to another if they are horizontally, vertically, or diagonally adjacent to each other on the map. Two areas are on the same island if and only if you can walk from one to the other possibly through other land areas. The marine area on the map is surrounded by the sea and therefore you cannot go outside of the area on foot.

You are requested to write a program that reads the map and counts the number of islands on it. For instance, the map in Figure B-1 includes three islands.

Input

The input consists of a series of datasets, each being in the following format.

> w h
>  c1,1 c1,2 ... c1,w
>  c2,1 c2,2 ... c2,w
>  ...
>  ch,1 ch,2 ... ch,w
>

w and h are positive integers no more than 50 that represent the width and the height of the given map, respectively. In other words, the map consists of w×h squares of the same size. w and h are separated by a single space.

ci, j is either 0 or 1 and delimited by a single space. If ci, j = 0, the square that is the i-th from the left and j-th from the top on the map represents a sea area. Otherwise, that is, if ci, j = 1, it represents a land area.

The end of the input is indicated by a line containing two zeros separated by a single space.

Output

For each dataset, output the number of the islands in a line. No extra characters should occur in the output.

Sample Input


1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0


Output for the Sample Input


0
1
1
3
1
9






Example

Input

1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0


Output

0
1
1
3
1
9
"""

def count_islands(map_data, width, height):
    def dfs(x, y):
        map_data[x][y] = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < height and 0 <= ny < width and (map_data[nx][ny] == 1):
                    dfs(nx, ny)

    cnt = 0
    for i in range(height):
        for j in range(width):
            if map_data[i][j] == 1:
                dfs(i, j)
                cnt += 1
    return cnt