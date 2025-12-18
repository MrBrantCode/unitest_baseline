"""
QUESTION:
Note that girls in Arpa’s land are really attractive.

Arpa loves overnight parties. In the middle of one of these parties Mehrdad suddenly appeared. He saw n pairs of friends sitting around a table. i-th pair consisted of a boy, sitting on the a_{i}-th chair, and his girlfriend, sitting on the b_{i}-th chair. The chairs were numbered 1 through 2n in clockwise direction. There was exactly one person sitting on each chair.

 [Image] 

There were two types of food: Kooft and Zahre-mar. Now Mehrdad wonders, was there any way to serve food for the guests such that:   Each person had exactly one type of food,  No boy had the same type of food as his girlfriend,  Among any three guests sitting on consecutive chairs, there was two of them who had different type of food. Note that chairs 2n and 1 are considered consecutive. 

Find the answer for the Mehrdad question. If it was possible, find some arrangement of food types that satisfies the conditions.


-----Input-----

The first line contains an integer n (1  ≤  n  ≤  10^5) — the number of pairs of guests.

The i-th of the next n lines contains a pair of integers a_{i} and b_{i} (1  ≤ a_{i}, b_{i} ≤  2n) — the number of chair on which the boy in the i-th pair was sitting and the number of chair on which his girlfriend was sitting. It's guaranteed that there was exactly one person sitting on each chair. 


-----Output-----

If there is no solution, print -1.

Otherwise print n lines, the i-th of them should contain two integers which represent the type of food for the i-th pair. The first integer in the line is the type of food the boy had, and the second integer is the type of food the girl had. If someone had Kooft, print 1, otherwise print 2.

If there are multiple solutions, print any of them.


-----Example-----
Input
3
1 4
2 5
3 6

Output
1 2
2 1
1 2
"""

def find_food_arrangement(n, pairs):
    """
    Determines if it's possible to serve food to guests such that:
    - Each person has exactly one type of food.
    - No boy has the same type of food as his girlfriend.
    - Among any three consecutive guests, there are two with different types of food.

    Parameters:
    n (int): The number of pairs of guests.
    pairs (list of tuples): A list of tuples where each tuple contains two integers representing the chair numbers of the boy and his girlfriend.

    Returns:
    list of tuples: A list of tuples where each tuple contains two integers representing the food types for a pair of guests. If no solution is possible, returns -1.
    """
    partner = [0] * (2 * n)
    pacani = []
    for a, b in pairs:
        pacan, telka = a - 1, b - 1
        partner[pacan] = telka
        partner[telka] = pacan
        pacani.append(pacan)
    
    khavka = [None] * (2 * n)
    for i in range(2 * n):
        while khavka[i] is None:
            khavka[i] = 1
            khavka[i ^ 1] = 2
            i = partner[i ^ 1]
    
    result = []
    for pacan in pacani:
        result.append((khavka[pacan], khavka[partner[pacan]]))
    
    return result