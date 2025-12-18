"""
QUESTION:
Implement the function `sortDescending` that sorts an array of integers in descending order using the Bubble Sort algorithm. The function should take an array of integers as input and return the sorted array. The function should use two nested loops and a conditional statement to swap elements. The outer loop should iterate over each element in the array, and the inner loop should iterate from the next index to the end of the array. The function should not use any built-in sorting functions.
"""

def sortDescending(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array