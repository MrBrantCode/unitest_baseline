"""
QUESTION:
Create a function called `square_and_divisible` that takes a list of integers as input. The function should return a new list containing the square of every element in the original list. If a square is divisible by 3, append "divisible by 3" to the new list. If a square is divisible by 5, append "divisible by 5" to the new list. If a square is divisible by both 3 and 5, append "divisible by both 3 and 5" to the new list. The function should remove any duplicates from the new list before returning it, without using any built-in functions like set().
"""

def square_and_divisible(numbers):
    new_list = []
    for num in numbers:
        square = num ** 2
        if square % 3 == 0 and square % 5 == 0:
            new_list.append(square)
            new_list.append("divisible by both 3 and 5")
        elif square % 3 == 0:
            new_list.append(square)
            new_list.append("divisible by 3")
        elif square % 5 == 0:
            new_list.append(square)
            new_list.append("divisible by 5")
        else:
            new_list.append(square)
    return new_list