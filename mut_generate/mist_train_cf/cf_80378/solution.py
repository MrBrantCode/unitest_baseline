"""
QUESTION:
Write a function `check_palindromic_tuples` that takes a one-dimensional array of integers as input and returns the count of unique palindromic pairs and triplets. A palindromic pair or triplet is defined as a sub-array that is equal to its reverse. The function should consider both pairs and triplets, and it should not count duplicate palindromic tuples.
"""

def check_palindromic_tuples(array):
    unique_tuples = set()
    count_palindromic_sequences = 0
    for sub_arr_len in [2, 3]:
        for i in range(len(array)- sub_arr_len + 1):
            sub_arr = array[i:i+sub_arr_len]
            if sub_arr[::-1] == sub_arr:
                unique_tuples.add(tuple(sub_arr))
    count_palindromic_sequences = len(unique_tuples)
    return count_palindromic_sequences