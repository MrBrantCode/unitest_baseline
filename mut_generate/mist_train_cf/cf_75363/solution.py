"""
QUESTION:
Create a function `organize_decimals` that takes a list of decimal fractions as input and returns a tuple containing the sum of the decimals and the sorted list of decimals in descending order. The function should exclude any repeating decimals within two decimal places and implement its own algorithms for sorting and summing without using pre-built functions.
"""

def organize_decimals(decimals):
    def check_repeating(number, decimals):
        # Check if number repeats within two decimal places in the list of decimals
        str_num = "{:.2f}".format(number)

        for dec in decimals:
            if "{:.2f}".format(dec) == str_num:
                return True
        return False

    def add_numbers(numbers):
        # Addition function
        sum_num = 0
        for num in numbers:
            sum_num += num
        return sum_num

    def bubble_sort(numbers):
        # Sorting function using Bubble Sort
        for i in range(len(numbers)):
            for j in range(len(numbers) - i - 1):
                if numbers[j] < numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers

    new_decimals = []
    for dec in decimals:
        if not check_repeating(dec, new_decimals):
            new_decimals.append(dec)
    
    sorted_decimals = bubble_sort(new_decimals)
    sum_decimals = add_numbers(sorted_decimals)
    
    return (sum_decimals, tuple(sorted_decimals))