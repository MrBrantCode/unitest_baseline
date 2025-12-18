"""
QUESTION:
Develop an algorithm with a time complexity of O(n^3) or better that identifies the three numbers with the largest sum in a given list of integers, excluding any negative numbers. The function should be named `find_largest_sum` and take a list of integers as input.
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