"""
QUESTION:
Write a function named `find_largest_sum` that takes a list of integers as input and returns the three numbers with the largest sum, excluding any negative numbers from consideration. The function must have a time complexity of O(n^3) or better.
"""

def find_largest_sum(numbers):
    numbers = [num for num in numbers if num >= 0]
    numbers.sort(reverse=True)
    largest_sum = 0
    largest_numbers = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                current_sum = numbers[i] + numbers[j] + numbers[k]
                if current_sum > largest_sum:
                    largest_sum = current_sum
                    largest_numbers = [numbers[i], numbers[j], numbers[k]]
    return largest_numbers