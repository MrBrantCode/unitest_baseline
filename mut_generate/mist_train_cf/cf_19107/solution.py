"""
QUESTION:
Implement a function called `insertion_sort_desc` that sorts an array of integers in descending order using the insertion sort algorithm. The function should take one argument, `array`, and return the sorted array. The function must use a for loop and a while loop to iterate through the array and swap elements as necessary.
"""

def insertion_sort_desc(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] < current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array