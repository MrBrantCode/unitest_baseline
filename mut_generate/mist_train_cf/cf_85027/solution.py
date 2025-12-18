"""
QUESTION:
Implement the `insertion_sort` function to sort a list of numbers in ascending order using the Insertion Sort algorithm. The function should take a list of numbers as input and return the sorted list.
"""

def insertionsort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i-1
        while j >=0 and key < numbers[j] :
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = key
    return numbers