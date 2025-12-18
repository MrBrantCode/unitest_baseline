"""
QUESTION:
Implement a function named `customSort` that sorts an array of numbers in ascending order using a custom sorting algorithm with a constant amount of extra memory and efficient handling for arrays with up to 1 million elements and duplicate numbers.
"""

def customSort(numbers):
    # Iterate through the array
    for i in range(len(numbers) - 1):
        # Find the minimum element in the remaining unsorted part of the array
        minIndex = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minIndex]:
                minIndex = j
        # Swap the minimum element with the first element in the unsorted part
        numbers[minIndex], numbers[i] = numbers[i], numbers[minIndex]
    
    # Return the sorted array
    return numbers