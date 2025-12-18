"""
QUESTION:
Write a function called ascendingOrder that takes a list of integers as input, removes any duplicates, and prints the numbers in ascending order. The function should achieve this with a time complexity of O(n log n) using a custom sorting algorithm, without relying on built-in sorting algorithms or data structures such as arrays or lists.
"""

def ascendingOrder(numbers):
    if not numbers:
        return

    uniqueNumbers = {}
    for number in numbers:
        if number not in uniqueNumbers:
            uniqueNumbers[number] = True

    maxNumber = max(numbers)
    sortedNumbers = []
    for i in range(maxNumber + 1):
        if i in uniqueNumbers:
            sortedNumbers.append(i)

    for number in sortedNumbers:
        print(number)