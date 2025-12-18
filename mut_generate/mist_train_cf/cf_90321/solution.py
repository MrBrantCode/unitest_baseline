"""
QUESTION:
Write a function called `determine_perfect_squares` that takes a list of integers as input and returns a new list with boolean values indicating whether each number in the input list is a perfect square or not. The function should not use any built-in or external libraries for square root calculation, power calculation, or arithmetic operations. The time complexity of the solution should be O(n) and the space complexity should be O(n), where n is the number of integers in the input list. The input list can contain up to 10^6 integers and each integer will be between 1 and 10^12.
"""

def determine_perfect_squares(numbers):
    def is_perfect_square(num):
        guess = 1
        while guess * guess < num:
            guess += 1
        return guess * guess == num

    results = []
    for num in numbers:
        results.append(is_perfect_square(num))
    return results