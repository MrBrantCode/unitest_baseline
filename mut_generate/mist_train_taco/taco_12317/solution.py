"""
QUESTION:
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:


       Each child must have at least one candy.
       Children with a higher rating get more candies than their neighbors.


What is the minimum candies you must give?

Example 1:


Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.


Example 2:


Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""

def minimum_candies(ratings: list[int]) -> int:
    if not ratings:
        return 0
    
    total = 1
    pre = 1
    decrease = 0
    
    for i in range(1, len(ratings)):
        if ratings[i] >= ratings[i - 1]:
            if decrease > 0:
                total += (1 + decrease) * decrease // 2
                if pre <= decrease:
                    total += decrease + 1 - pre
                decrease = 0
                pre = 1
            if ratings[i] == ratings[i - 1]:
                total += 1
                pre = 1
            else:
                pre += 1
                total += pre
        else:
            decrease += 1
    
    if decrease > 0:
        total += (1 + decrease) * decrease // 2
        if pre <= decrease:
            total += decrease + 1 - pre
    
    return total