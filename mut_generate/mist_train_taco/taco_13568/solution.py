"""
QUESTION:
Two little greedy bears have found two pieces of cheese in the forest of weight a and b grams, correspondingly. The bears are so greedy that they are ready to fight for the larger piece. That's where the fox comes in and starts the dialog: "Little bears, wait a little, I want to make your pieces equal" "Come off it fox, how are you going to do that?", the curious bears asked. "It's easy", said the fox. "If the mass of a certain piece is divisible by two, then I can eat exactly a half of the piece. If the mass of a certain piece is divisible by three, then I can eat exactly two-thirds, and if the mass is divisible by five, then I can eat four-fifths. I'll eat a little here and there and make the pieces equal". 

The little bears realize that the fox's proposal contains a catch. But at the same time they realize that they can not make the two pieces equal themselves. So they agreed to her proposal, but on one condition: the fox should make the pieces equal as quickly as possible. Find the minimum number of operations the fox needs to make pieces equal.


-----Input-----

The first line contains two space-separated integers a and b (1 ≤ a, b ≤ 10^9). 


-----Output-----

If the fox is lying to the little bears and it is impossible to make the pieces equal, print -1. Otherwise, print the required minimum number of operations. If the pieces of the cheese are initially equal, the required number is 0.


-----Examples-----
Input
15 20

Output
3

Input
14 8

Output
-1

Input
6 6

Output
0
"""

def min_operations_to_equalize_cheese(a: int, b: int) -> int:
    # Initialize counters for each divisor
    x, y, z = 0, 0, 0
    X, Y, Z = 0, 0, 0
    
    # Count the number of operations needed to reduce 'a'
    while a % 2 == 0:
        a //= 2
        x += 1
    while a % 3 == 0:
        a //= 3
        y += 1
    while a % 5 == 0:
        a //= 5
        z += 1
    
    # Count the number of operations needed to reduce 'b'
    while b % 2 == 0:
        b //= 2
        X += 1
    while b % 3 == 0:
        b //= 3
        Y += 1
    while b % 5 == 0:
        b //= 5
        Z += 1
    
    # If the reduced values of 'a' and 'b' are not equal, it's impossible
    if a != b:
        return -1
    
    # Calculate the minimum number of operations needed
    return max(X, x) - min(X, x) + max(y, Y) - min(y, Y) + max(z, Z) - min(z, Z)