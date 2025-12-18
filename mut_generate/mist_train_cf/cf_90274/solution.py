"""
QUESTION:
Create a function `generate_numbers` that takes a positive integer `N` as input and returns a list of `N` unique randomly generated numbers between 0 and 100, in ascending order. The function should have a time complexity of O(N), not use any external libraries for random number generation, and implement its own sorting without using built-in sorting functions. The function should return an empty list for `N < 0` and print an error message for `N > 100`.
"""

def generate_numbers(N):
    if N < 0:
        return []
    elif N > 100:
        print("N should be less than or equal to 100.")
        return []
    
    numbers = []
    for i in range(N):
        num = (110 * i + N) % 101
        numbers.append(num)
    
    # Implementing Bubble Sort
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers