"""
QUESTION:
Write a function `closest_product(u, N)` that finds the pair of elements in the array `u` whose product is closest to the integer `N`. If there are multiple pairs with the same absolute difference from `N`, return the pair with the smallest product. The input array `u` has at least two elements, and all elements in the array and the integer `N` are within the integer range.
"""

def closest_product(u, N):
    u.sort()
    closest_pair = []
    min_diff = float('inf')

    for i in range(len(u)):
        for j in range(i + 1, len(u)):
            product = u[i] * u[j]
            diff = abs(product - N)
            if diff < min_diff or (diff == min_diff and product < u[0] * u[1]):
                min_diff = diff
                closest_pair = [u[i], u[j]]

    return closest_pair