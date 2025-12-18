"""
QUESTION:
Develop a function `count_pairs` that takes an array of integers and an integer `k` as inputs. The function should return the count of unique pairs of numbers within the array where one number divided by the other results in an exact multiple of `k`. The function should consider both possible orders of division for each pair.
"""

def count_pairs(array, k):
    count = 0
    array_length = len(array)
    for i in range(array_length):
        for j in range(i+1, array_length):
            if array[i]%array[j]==0 and array[i]//array[j]==k:
                count += 1
            if array[j]%array[i]==0 and array[j]//array[i]==k:
                count += 1
    return count