"""
QUESTION:
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True



Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False



Note:

The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    # Calculate the maximum number of flowers that can be planted
    max_flowers = len(flowerbed) // 2 + 1
    
    # If the number of existing flowers plus the new flowers exceeds the maximum, return False
    if flowerbed.count(1) + n > max_flowers:
        return False
    
    # Iterate through the flowerbed to check if we can place the flowers
    pos = 0
    while pos < len(flowerbed):
        if n == 0:
            return True
        if pos + 1 < len(flowerbed):
            if flowerbed[pos] == 0 and flowerbed[pos + 1] == 0:
                n -= 1
                pos += 2
            elif flowerbed[pos] == 1:
                pos += 2
            else:
                pos += 3
        elif flowerbed[pos] == 0:
            n -= 1
            pos += 2
    
    return n == 0