"""
QUESTION:
A star map in Berland is a checked field n × m squares. In each square there is or there is not a star. The favourite constellation of all Berland's astronomers is the constellation of the Cross. This constellation can be formed by any 5 stars so, that for some integer x (radius of the constellation) the following is true: 

  * the 2nd is on the same vertical line as the 1st, but x squares up 
  * the 3rd is on the same vertical line as the 1st, but x squares down 
  * the 4th is on the same horizontal line as the 1st, but x squares left 
  * the 5th is on the same horizontal line as the 1st, but x squares right 



Such constellations can be very numerous, that's why they are numbered with integers from 1 on the following principle: when two constellations are compared, the one with a smaller radius gets a smaller index; if their radii are equal — the one, whose central star if higher than the central star of the other one; if their central stars are at the same level — the one, whose central star is to the left of the central star of the other one.

Your task is to find the constellation with index k by the given Berland's star map.

Input

The first line contains three integers n, m and k (1 ≤ n, m ≤ 300, 1 ≤ k ≤ 3·107) — height and width of the map and index of the required constellation respectively. The upper-left corner has coordinates (1, 1), and the lower-right — (n, m). Then there follow n lines, m characters each — description of the map. j-th character in i-th line is «*», if there is a star in the corresponding square, and «.» if this square is empty.

Output

If the number of the constellations is less than k, output -1. Otherwise output 5 lines, two integers each — coordinates of the required constellation. Output the stars in the following order: central, upper, lower, left, right.

Examples

Input

5 6 1
....*.
...***
....*.
..*...
.***..


Output

2 5
1 5
3 5
2 4
2 6


Input

5 6 2
....*.
...***
....*.
..*...
.***..


Output

-1


Input

7 7 2
...*...
.......
...*...
*.***.*
...*...
.......
...*...


Output

4 4
1 4
7 4
4 1
4 7
"""

def find_kth_constellation(n, m, k, star_map):
    a = [tuple(map(lambda c: c == '*', row)) for row in star_map]
    cnt = [0] * 400
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not a[i][j]:
                continue
            for (rad, ui, di, lj, rj) in zip(range(1, 400), range(i - 1, -1, -1), range(i + 1, n), range(j - 1, -1, -1), range(j + 1, m)):
                if all((a[ui][j], a[di][j], a[i][lj], a[i][rj])):
                    cnt[rad] += 1
    
    rad = -1
    for i in range(300):
        cnt[i + 1] += cnt[i]
        if cnt[i] >= k:
            rad = i
            k -= cnt[i - 1]
            break
    else:
        return -1
    
    for i in range(rad, n - rad):
        for j in range(rad, m - rad):
            if all((a[i][j], a[i - rad][j], a[i + rad][j], a[i][j - rad], a[i][j + rad])):
                k -= 1
                if k == 0:
                    return [
                        (i + 1, j + 1),
                        (i - rad + 1, j + 1),
                        (i + rad + 1, j + 1),
                        (i + 1, j - rad + 1),
                        (i + 1, j + rad + 1)
                    ]
    
    return -1