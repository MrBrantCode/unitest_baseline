"""
QUESTION:
Write a function `poorPigs` that takes three parameters: `buckets`, `minutesToDie`, and `minutesToTest`. The function should return a tuple containing the minimum number of pigs required to figure out which bucket is poisonous within the allotted time and the total amount of liquid consumed by the pigs. Assume each pig consumes 1 liter of liquid from each bucket it is fed. The function should satisfy the constraints 1 <= buckets <= 1000, 1 <= minutesToDie <= minutesToTest <= 100.
"""

def poorPigs(buckets, minutesToDie, minutesToTest):
    pigs = 0
    while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        pigs += 1
    return pigs, buckets * pigs