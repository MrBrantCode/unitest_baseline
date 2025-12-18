"""
QUESTION:
You are given a cubic storeroom with width, length, and height equal to `n` units, and `n` boxes each with a unit side length. The boxes can be placed anywhere on the floor, and if box `x` is placed on top of box `y`, each side of the four vertical sides of box `y` must be adjacent to another box or the wall. 

Write a function `minimumBoxes(n)` that returns the minimum number of boxes touching the floor and their coordinates. The function should take an integer `n` as input and return a tuple, where the first element is the minimum number of boxes touching the floor and the second element is a list of coordinates of the boxes touching the floor in the format (x, y), where x is the distance from the left wall and y is the distance from the back wall.

Constraints: `1 <= n <= 10^9`
"""

def minimumBoxes(n):
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        k = (mid + 1) // 2
        a1 = k * k
        a2 = (mid - k) * (mid - k)
        b1 = k * (k - 1) // 2
        b2 = (mid - k) * (mid - k + 1) // 2
        count = a1 + a2 + 2 * (b1 + b2)
        if count >= n * n * n:
            r = mid - 1
        else:
            l = mid + 1

    return l, [(i, 0) for i in range(l)]