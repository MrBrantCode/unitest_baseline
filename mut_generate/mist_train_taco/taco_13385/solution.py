"""
QUESTION:
Mary has just graduated from one well-known University and is now attending celebration party. Students like to dream of a beautiful life, so they used champagne glasses to construct a small pyramid. The height of the pyramid is n. The top level consists of only 1 glass, that stands on 2 glasses on the second level (counting from the top), then 3 glasses on the third level and so on.The bottom level consists of n glasses.

Vlad has seen in the movies many times how the champagne beautifully flows from top levels to bottom ones, filling all the glasses simultaneously. So he took a bottle and started to pour it in the glass located at the top of the pyramid.

Each second, Vlad pours to the top glass the amount of champagne equal to the size of exactly one glass. If the glass is already full, but there is some champagne flowing in it, then it pours over the edge of the glass and is equally distributed over two glasses standing under. If the overflowed glass is at the bottom level, then the champagne pours on the table. For the purpose of this problem we consider that champagne is distributed among pyramid glasses immediately. Vlad is interested in the number of completely full glasses if he stops pouring champagne in t seconds.

Pictures below illustrate the pyramid consisting of three levels. [Image] [Image] 


-----Input-----

The only line of the input contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 10 000) — the height of the pyramid and the number of seconds Vlad will be pouring champagne from the bottle.


-----Output-----

Print the single integer — the number of completely full glasses after t seconds.


-----Examples-----
Input
3 5

Output
4

Input
4 8

Output
6



-----Note-----

In the first sample, the glasses full after 5 seconds are: the top glass, both glasses on the second level and the middle glass at the bottom level. Left and right glasses of the bottom level will be half-empty.
"""

def count_full_glasses(n, t):
    # Initialize the pyramid with glasses set to 0
    pyramid = [[0 for _ in range(i + 1)] for i in range(n)]
    
    def add(x, r, c):
        pyramid[r][c] += x
        amount = pyramid[r][c]
        if amount > 1 and r + 1 < n:
            amount -= 1
            pyramid[r + 1][c] += amount / 2
            pyramid[r + 1][c + 1] += amount / 2
            pyramid[r][c] = 1
    
    # Pour champagne for t seconds
    for _ in range(t):
        add(1, 0, 0)
        for row in range(n):
            for col in range(row + 1):
                add(0, row, col)
    
    # Count the number of completely full glasses
    total = 0
    for row in range(n):
        for col in range(row + 1):
            if pyramid[row][col] >= 1:
                total += 1
    
    return total