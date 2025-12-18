"""
QUESTION:
Iahub and his friend Floyd have started painting a wall. Iahub is painting the wall red and Floyd is painting it pink. You can consider the wall being made of a very large number of bricks, numbered 1, 2, 3 and so on. 

Iahub has the following scheme of painting: he skips x - 1 consecutive bricks, then he paints the x-th one. That is, he'll paint bricks x, 2·x, 3·x and so on red. Similarly, Floyd skips y - 1 consecutive bricks, then he paints the y-th one. Hence he'll paint bricks y, 2·y, 3·y and so on pink.

After painting the wall all day, the boys observed that some bricks are painted both red and pink. Iahub has a lucky number a and Floyd has a lucky number b. Boys wonder how many bricks numbered no less than a and no greater than b are painted both red and pink. This is exactly your task: compute and print the answer to the question. 


-----Input-----

The input will have a single line containing four integers in this order: x, y, a, b. (1 ≤ x, y ≤ 1000, 1 ≤ a, b ≤ 2·10^9, a ≤ b).


-----Output-----

Output a single integer — the number of bricks numbered no less than a and no greater than b that are painted both red and pink.


-----Examples-----
Input
2 3 6 18

Output
3


-----Note-----

Let's look at the bricks from a to b (a = 6, b = 18). The bricks colored in red are numbered 6, 8, 10, 12, 14, 16, 18. The bricks colored in pink are numbered 6, 9, 12, 15, 18. The bricks colored in both red and pink are numbered with 6, 12 and 18.
"""

def count_bricks_painted_both_colors(x: int, y: int, a: int, b: int) -> int:
    """
    Counts the number of bricks numbered no less than 'a' and no greater than 'b'
    that are painted both red and pink.

    Parameters:
    x (int): The step size for Iahub's painting scheme.
    y (int): The step size for Floyd's painting scheme.
    a (int): The starting number of the range of bricks.
    b (int): The ending number of the range of bricks.

    Returns:
    int: The number of bricks painted both red and pink within the range [a, b].
    """
    
    def gcd(x, y):
        if y % x == 0:
            return x
        else:
            return gcd(y % x, x)
    
    g = gcd(min(x, y), max(x, y))
    l = x * y // g
    
    i = a
    while i < a + l:
        if i > b:
            break
        if i % l == 0:
            break
        i += 1
    
    if b >= i:
        return (b - i) // l + 1
    else:
        return 0