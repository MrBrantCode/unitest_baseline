"""
QUESTION:
Correct the erroneous code in the bubble_sort function and use it to sort a list of numbers in ascending order without using the built-in sort() function or any other sorting algorithm. The function should swap elements correctly to achieve the desired output.
"""

def entrance(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers