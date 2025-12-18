"""
QUESTION:
Heidi the Cow is aghast: cracks in the northern Wall? Zombies gathering outside, forming groups, preparing their assault? This must not happen! Quickly, she fetches her HC^2 (Handbook of Crazy Constructions) and looks for the right chapter:

How to build a wall:  Take a set of bricks.  Select one of the possible wall designs. Computing the number of possible designs is left as an exercise to the reader.  Place bricks on top of each other, according to the chosen design. 

This seems easy enough. But Heidi is a Coding Cow, not a Constructing Cow. Her mind keeps coming back to point 2b. Despite the imminent danger of a zombie onslaught, she wonders just how many possible walls she could build with up to n bricks.

A wall is a set of wall segments as defined in the easy version. How many different walls can be constructed such that the wall consists of at least 1 and at most n bricks? Two walls are different if there exist a column c and a row r such that one wall has a brick in this spot, and the other does not.

Along with n, you will be given C, the width of the wall (as defined in the easy version). Return the number of different walls modulo 10^6 + 3.


-----Input-----

The first line contains two space-separated integers n and C, 1 ≤ n ≤ 500000, 1 ≤ C ≤ 200000.


-----Output-----

Print the number of different walls that Heidi could build, modulo 10^6 + 3.


-----Examples-----
Input
5 1

Output
5

Input
2 2

Output
5

Input
3 2

Output
9

Input
11 5

Output
4367

Input
37 63

Output
230574



-----Note-----

The number 10^6 + 3 is prime.

In the second sample case, the five walls are: 

            B        B

B., .B, BB, B., and .B



In the third sample case, the nine walls are the five as in the second sample case and in addition the following four: 

B    B

B    B  B        B

B., .B, BB, and BB
"""

def count_possible_walls(n: int, C: int) -> int:
    """
    Calculate the number of different walls that can be constructed with up to n bricks and width C,
    modulo 10^6 + 3.

    Parameters:
    n (int): The maximum number of bricks available.
    C (int): The width of the wall.

    Returns:
    int: The number of different walls modulo 10^6 + 3.
    """
    mod = 10 ** 6 + 3
    inv = [0, 1]
    
    # Calculate modular inverses
    for i in range(2, max(n, C) + 1):
        inv.append(inv[mod % i] * (mod - mod // i) % mod)
    
    # Calculate the number of possible walls
    ans = 1
    for i in range(1, n + C + 1):
        ans = ans * i % mod
    for i in range(1, C + 1):
        ans = ans * inv[i] % mod
    for i in range(1, n + 1):
        ans = ans * inv[i] % mod
    
    ans += mod - 1
    ans %= mod
    
    return ans