"""
QUESTION:
Write a function `first_odd_occurrences(arr)` where 
- arr: a list of "n" sub-lists (1<=n<=10^4). Each sublist has "m" integers (1<=m<=10^4). 

Your task is to find the first integer in each sub-array that appears an odd number of times. If multiple numbers have odd frequencies, return the number with the maximum odd frequency. If there are multiple numbers with the same maximum odd frequency, return the one which first appeared in the sub-array. 

Output
It returns a list of "n" integers, representing the first integer from each sub-array that appears an odd number of times.

Your solution should have optimal time and space complexity.
"""

def first_odd_occurrences(arr):
    result = []
    for sub_arr in arr:
        freq = {}
        for num in sub_arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num in sub_arr:
            if freq[num] % 2 == 1:
                result.append(num)
                break
    return result