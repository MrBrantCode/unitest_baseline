"""
QUESTION:
Implement a recursive function `print_odd_or_even` that takes two parameters `start` and `end` representing the range of odd numbers to iterate through, prints "even" or "odd" for each number based on its divisibility by 2, and meets the following requirements: 

The function should iterate through odd numbers only. 
The time complexity should be O(n), where n is the maximum number in the range.
The space complexity should be O(1), meaning the program should not use any additional data structures that scale with the input size.
"""

def print_odd_or_even(start, end):
    if start > end:
        return

    if start % 2 == 0:
        print("even")
    else:
        print("odd")

    print_odd_or_even(start + 2, end)