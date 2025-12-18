"""
QUESTION:
Write a function named `find_odd_numbers` that takes a list of numbers as input. The function should return a new list containing only the odd numbers found in the input list, handle non-integer values and negative numbers, and also print the number of odd numbers found, their positions in the original list, and the total sum of the odd numbers.
"""

def find_odd_numbers(my_list):
    odd_numbers = []
    odd_positions = []
    for i in range(len(my_list)):
        if isinstance(my_list[i], (int, float)):
            if my_list[i] % 2 != 0:
                odd_numbers.append(my_list[i])
                odd_positions.append(i)
    
    print("Odd numbers found:", len(odd_numbers))
    print("Positions:", odd_positions)
    print("New list:", odd_numbers)
    print("Sum of odd numbers:", sum(odd_numbers))
    
    return odd_numbers