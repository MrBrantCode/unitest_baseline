"""
QUESTION:
Write a recursive function named `print_odd_or_even` that takes two parameters: `start` and `end`, representing the range of odd numbers to iterate through. The function should print "even" if the current number is divisible by 2 and "odd" if not. The function should only iterate through odd numbers and terminate after printing the result. The time complexity should be O(n), where n is the maximum number in the range, and the space complexity should be O(1), without using any additional data structures that scale with the input size.
"""

def print_odd_or_even(start, end):
    if start > end:
        return

    if start % 2 == 0:
        print("even")
    else:
        print("odd")

    print_odd_or_even(start + 2, end)