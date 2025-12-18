"""
QUESTION:
As part of this Kata, you need to find the length of the sequence in an array, between the first and the second occurrence of a specified number.

For example, for a given array `arr`

    [0, -3, 7, 4, 0, 3, 7, 9]
    
Finding length between two `7`s like
    
    lengthOfSequence([0, -3, 7, 4, 0, 3, 7, 9], 7)
    
would return `5`.

For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.

If there are less or more than two occurrences of the number to search for, return `0`, or in Haskell, `Nothing`.
"""

def find_sequence_length(arr, n):
    # Check if the number of occurrences of `n` is exactly 2
    if arr.count(n) != 2:
        return 0
    
    # Find the index of the first occurrence of `n`
    first_index = arr.index(n)
    
    # Find the index of the second occurrence of `n`
    second_index = arr.index(n, first_index + 1)
    
    # Calculate the length of the sequence between the two occurrences
    return second_index - first_index + 1