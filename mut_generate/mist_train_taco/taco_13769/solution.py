"""
QUESTION:
Not to be confused with chessboard.

 [Image] 


-----Input-----

The first line of input contains a single integer N (1 ≤ N ≤ 100) — the number of cheeses you have.

The next N lines describe the cheeses you have. Each line contains two space-separated strings: the name of the cheese and its type. The name is a string of lowercase English letters between 1 and 10 characters long. The type is either "soft" or "hard. All cheese names are distinct.


-----Output-----

Output a single number.


-----Examples-----
Input
9
brie soft
camembert soft
feta soft
goat soft
muenster soft
asiago hard
cheddar hard
gouda hard
swiss hard

Output
3

Input
6
parmesan hard
emmental hard
edam hard
colby hard
gruyere hard
asiago hard

Output
4
"""

from math import sqrt, ceil

def calculate_cheese_arrangement(n, cheeses):
    x = cheeses.count('soft')
    y = cheeses.count('hard')
    
    if (abs(x - y) == 1 or x == y) and int(sqrt(n) + 0.5) ** 2 == n:
        return int(sqrt(n))
    else:
        ma = max(x, y)
        t = ma * 2
        if t - 1 < n:
            return ceil(sqrt(t))
        else:
            return min(ceil(sqrt(t)), ceil(sqrt(t - 1)))