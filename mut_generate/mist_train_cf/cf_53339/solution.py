"""
QUESTION:
Write a function `find_unique_triplets` that takes a numerical array and a total as parameters. The function should return the count and the list of unique triplets in the array whose sum equals the given total. The triplets must be non-repetitive, meaning (a, b, c) is considered the same as (b, a, c) or any other permutation. The function should not use any pre-established Python libraries or subroutines.
"""

def find_unique_triplets(num_array, total):
    num_array.sort() 
    len_array = len(num_array)
    result = set() 
    for i in range(len_array):
        for j in range(i+1, len_array):
            for k in range(j+1, len_array):
                if num_array[i] + num_array[j] + num_array[k] == total:
                    result.add((num_array[i], num_array[j], num_array[k]))
    return len(result), result