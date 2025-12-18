"""
QUESTION:
Write a function `numPairsDivisibleBy90` that takes a list of integers `time` representing song durations in seconds as input and returns the number of triplets of songs whose combined duration is divisible by 90. The function should run in O(n) time, where n is the length of the input list. The input list `time` satisfies the following constraints: `1 <= time.length <= 6 * 10^4` and `1 <= time[i] <= 500`.
"""

from typing import List

def numPairsDivisibleBy90(time: List[int]) -> int:
    mod_count = [0]*90
    
    for t in time:
        mod_count[t % 90] += 1
    
    result = 0

    result += mod_count[0]*(mod_count[0]-1)*(mod_count[0]-2)//6
    
    for i in range(1, 45):
        j = 90 - i
        result += mod_count[i]*mod_count[j]*(mod_count[j]-1)//2
        result += mod_count[i]*(mod_count[i]-1)//2*mod_count[j]
        
    result += mod_count[45]*(mod_count[45]-1)*(mod_count[45]-2)//6
    
    return result