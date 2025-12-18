"""
QUESTION:
Can Place Flowers with Constraints

You are given three inputs: `flowerbed`, `weight`, and `n`. `flowerbed` and `weight` are integer arrays of the same length, where `flowerbed[i]` is 0 if the plot is empty and 1 if the plot is not empty, and `weight[i]` is an integer between 1 and 100 representing the weight capacity of the plot. `n` is an integer representing the number of new flowers to be planted.

Write a function `canPlantFlowers(flowerbed, weight, n)` that returns True if it is possible to plant `n` new flowers in the `flowerbed` without violating the no-adjacent-flowers rule and the weight constraints, and False otherwise.

Constraints:

* 1 <= flowerbed.length, weight.length <= 2 * 10^4
* flowerbed[i] is 0 or 1
* weight[i] is an integer between 1 and 100
* There are no two adjacent flowers in `flowerbed`
* 0 <= n <= flowerbed.length
* The sum of `n` and the number of 1s in `flowerbed` should not exceed the sum of `weight`
"""

def canPlaceFlowers(flowerbed, weight, n):
    length = len(flowerbed)
    canPlant = 0
    for i in range(length):
        if flowerbed[i] == 0 and flowerbed[i] + n <= weight[i] and (i == 0 or flowerbed[i-1] == 0) and (i == length - 1 or flowerbed[i+1] == 0):
            canPlant += 1
        if canPlant >= n:
            return True
    return False