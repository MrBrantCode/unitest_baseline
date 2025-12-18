"""
QUESTION:
Implement the function `countPerfectMeals(deliciousness)` to count the number of perfect meals. A perfect meal is a pair of two different dishes with a total deliciousness that is a perfect cube. The total number of perfect meals is calculated by considering all possible pairs of dishes. 

Restrictions:
- The function should take a list of integers `deliciousness` as input, representing the deliciousness of each dish.
- The function should return the total number of perfect meals modulo `10**9 + 7`.
- Helper function `isPerfectCube(n)` can be used to check if a number is a perfect cube.
"""

import math

def countPerfectMeals(deliciousness):
    MOD = 10**9 + 7
    count ={}
    # count frequency of each deliciousness
    for value in deliciousness:
        count[value] = count.get(value, 0) + 1
    res = 0
    # for each pair, check if we have their complement
    for i in count.keys():
        for j in count.keys():
            if i == j and count[i] < 3: # if i equals to j, need 3 duplicates
                continue
            if isPerfectCube(i*3) or isPerfectCube(i*2 + j) or isPerfectCube(i + j*2):
                if i != j: # if i different than j 
                    res += count[i] * count[j] * (count[i] - 1) // 2
                else:
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
    return res % MOD

def isPerfectCube(n):
    cube_root = round(n ** (1/3))
    return cube_root ** 3 == n