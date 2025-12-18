"""
QUESTION:
Write a function `minimum_changes_to_palindrome(arr, limit)` that determines the minimum number of elements that need to be changed to transform the array into a palindrome with a constraint on the number of unique elements that can be modified. The function should take two parameters: an integer array `arr` and an integer `limit`, where `limit` is the maximum number of unique elements that can be modified. The function should return the minimum number of elements that need to be changed.
"""

def minimum_changes_to_palindrome(arr, limit):
    i, j = 0, len(arr) - 1 #start and end pointers
    changes = 0
    unique_elements = set() 

    while i <= j: 
        if arr[i] != arr[j]: 
            changes += 1
            if arr[i] not in unique_elements: #check for unique modifications constraint
                limit -= 1
                if limit < 0: 
                    return changes
                unique_elements.add(arr[i])
            arr[
              j] = arr[i] #make both ends same by replacing the larger one with the smaller one
        i += 1
        j -= 1

    return changes