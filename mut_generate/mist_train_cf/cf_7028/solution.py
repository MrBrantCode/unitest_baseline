"""
QUESTION:
Implement a function named `recursive_sum` to calculate the sum of all elements in a given 3D array without using loops or built-in sum functions. The input 3D array can be of any size. The function should return the total sum of all elements in the array.
"""

def recursive_sum(arr, i=0, j=0, k=0):
    # Base case: if we reach the end of the array, return 0
    if i == len(arr) or j == len(arr[i]) or k == len(arr[i][j]):
        return 0
    
    # Calculate the sum of current element and the sum of the rest of the array
    current_sum = arr[i][j][k]
    remaining_sum = recursive_sum(arr, i, j, k + 1)
    if k == len(arr[i][j]) - 1:
        remaining_sum += recursive_sum(arr, i, j + 1, 0)
    if j == len(arr[i]) - 1 and k == len(arr[i][j]) - 1:
        remaining_sum += recursive_sum(arr, i + 1, 0, 0)
    
    # Return the sum of current element and the remaining sum
    return current_sum + remaining_sum