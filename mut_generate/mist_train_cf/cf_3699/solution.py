"""
QUESTION:
Implement a function `calculate_sum` that takes a list of positive integers between 1 and 100 and returns the sum of the numbers after applying the following conditions: exclude numbers divisible by both 3 and 5, multiply numbers divisible by 7 by 2, add half of numbers divisible by either 3 or 5 but not both, and subtract one-third of numbers divisible by both 3 and 5. The final sum should be rounded to the nearest hundredth.
"""

def calculate_sum(numbers):
    def helper(acc, num):
        if num % 3 == 0 and num % 5 == 0:  # divisible by both 3 and 5
            acc -= num / 3
        elif num % 7 == 0:  # divisible by 7
            acc += num * 2
        elif num % 3 == 0 or num % 5 == 0:  # divisible by either 3 or 5 but not both
            acc += num / 2
        else:
            acc += num
        return acc

    return round(sum(helper(0, num) for num in numbers), 2)