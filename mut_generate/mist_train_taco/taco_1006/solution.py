"""
QUESTION:
Fox Ciel has some flowers: r red flowers, g green flowers and b blue flowers. She wants to use these flowers to make several bouquets. There are 4 types of bouquets:

  To make a "red bouquet", it needs 3 red flowers.  To make a "green bouquet", it needs 3 green flowers.  To make a "blue bouquet", it needs 3 blue flowers.  To make a "mixing bouquet", it needs 1 red, 1 green and 1 blue flower. 

Help Fox Ciel to find the maximal number of bouquets she can make.


-----Input-----

The first line contains three integers r, g and b (0 ≤ r, g, b ≤ 10^9) — the number of red, green and blue flowers.


-----Output-----

Print the maximal number of bouquets Fox Ciel can make.


-----Examples-----
Input
3 6 9

Output
6

Input
4 4 4

Output
4

Input
0 0 0

Output
0



-----Note-----

In test case 1, we can make 1 red bouquet, 2 green bouquets and 3 blue bouquets.

In test case 2, we can make 1 red, 1 green, 1 blue and 1 mixing bouquet.
"""

def max_bouquets(r, g, b):
    # Sort the number of flowers to easily access the smallest, middle, and largest counts
    flowers = sorted([r, g, b])
    
    # If any flower count is zero, we can only make bouquets from the remaining two types
    if flowers[0] == 0:
        return flowers[1] // 3 + flowers[2] // 3
    
    # Calculate the number of bouquets by considering different strategies
    # Strategy 1: Use the smallest count to make mixing bouquets
    ans = flowers[0]
    flowers[1] -= ans
    flowers[2] -= ans
    ans += flowers[1] // 3 + flowers[2] // 3
    
    # Strategy 2: Use the smallest count minus 1 to make mixing bouquets
    ans1 = flowers[0] - 1
    flowers[1] -= ans1
    flowers[2] -= ans1
    ans1 += flowers[1] // 3 + flowers[2] // 3
    
    # Strategy 3: Use the smallest count minus 2 to make mixing bouquets
    ans2 = flowers[0] - 2
    flowers[1] -= ans2
    flowers[2] -= ans2
    ans2 += flowers[1] // 3 + flowers[2] // 3
    
    # Return the maximum number of bouquets from the three strategies
    return max(ans, ans1, ans2)