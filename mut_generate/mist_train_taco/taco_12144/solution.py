"""
QUESTION:
A revolution took place on the Buka Island. New government replaced the old one. The new government includes n parties and each of them is entitled to some part of the island according to their contribution to the revolution. However, they can't divide the island.

The island can be conventionally represented as two rectangles a × b and c × d unit squares in size correspondingly. The rectangles are located close to each other. At that, one of the sides with the length of a and one of the sides with the length of c lie on one line. You can see this in more details on the picture.

<image>

The i-th party is entitled to a part of the island equal to xi unit squares. Every such part should fully cover several squares of the island (it is not allowed to cover the squares partially) and be a connected figure. A "connected figure" presupposes that from any square of this party one can move to any other square of the same party moving through edge-adjacent squares also belonging to that party.

Your task is to divide the island between parties.

Input

The first line contains 5 space-separated integers — a, b, c, d and n (1 ≤ a, b, c, d ≤ 50, b ≠ d, 1 ≤ n ≤ 26). The second line contains n space-separated numbers. The i-th of them is equal to number xi (1 ≤ xi ≤ a × b + c × d). It is guaranteed that <image>.

Output

If dividing the island between parties in the required manner is impossible, print "NO" (without the quotes). Otherwise, print "YES" (also without the quotes) and, starting from the next line, print max(b, d) lines each containing a + c characters. To mark what square should belong to what party, use lowercase Latin letters. For the party that is first in order in the input data, use "a", for the second one use "b" and so on. Use "." for the squares that belong to the sea. The first symbol of the second line of the output data should correspond to the square that belongs to the rectangle a × b. The last symbol of the second line should correspond to the square that belongs to the rectangle c × d.

If there are several solutions output any.

Examples

Input

3 4 2 2 3
5 8 3


Output

YES
aaabb
aabbb
cbb..
ccb..


Input

3 2 1 4 4
1 2 3 4


Output

YES
abbd
cccd
...d
...d
"""

def divide_island(a, b, c, d, n, X):
    def solve(x0, y0, dx, X):
        for (i, x) in enumerate(X):
            while x > 0:
                x -= 1
                m[y0][x0] = i
                x0 += dx
                if x == 0 and i == len(X) - 1:
                    break
                if x0 == -1:
                    y0 += 1
                    x0 = 0
                    dx *= -1
                    if m[y0][x0] == -1:
                        return False
                elif x0 == a + c:
                    y0 += 1
                    x0 = a + c - 1
                    dx *= -1
                    if m[y0][x0] == -1:
                        return False
                elif m[y0][x0] == -1:
                    y0 += 1
                    x0 -= dx
                    dx *= -1
        return True

    m = [[-1] * (a + c) for _ in range(max(b, d))]
    
    if b < d:
        for i in range(b, d):
            for j in range(a):
                m[i][j] = -1
    else:
        for i in range(d, b):
            for j in range(a, a + c):
                m[i][j] = -1
    
    if not solve(a + c - 1, 0, -1, X):
        if not solve(0, 0, 1, X):
            return "NO"
    
    result = []
    for x in m:
        result.append(''.join([chr(c + 97) if c >= 0 else '.' for c in x]))
    
    return result