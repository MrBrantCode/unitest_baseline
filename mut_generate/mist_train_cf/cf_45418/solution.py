"""
QUESTION:
Create a function `count_and_sum_odds` that takes a two-dimensional array of integers as input and returns a list of dictionaries, where each dictionary contains the count of odd numbers in each sub-array and the sum of all odd numbers in that sub-array, along with a final dictionary containing the total sum of all odd numbers in the entire array.
"""

def count_and_sum_odds(arr):
    results = []
    total = 0
    for i, subarr in enumerate(arr, 1):
        odd_numbers = [num for num in subarr if num % 2 != 0]
        sum_of_odd_numbers = sum(odd_numbers)
        total += sum_of_odd_numbers
        results.append({"Odd numbers in {}th array".format(i): len(odd_numbers), "Sum": sum_of_odd_numbers})
    results.append({"Total sum of all odd numbers": total})
    return results