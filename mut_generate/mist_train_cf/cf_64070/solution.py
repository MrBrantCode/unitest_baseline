"""
QUESTION:
Create a function named 'multi_dimensional_input' that accepts a list of dictionaries, where each dictionary contains two keys: 'numbers' (a list of integers) and 'types' (a string stating either 'odd' or 'even'). The function should return a dictionary with keys as 'odd' and 'even' and the corresponding values as tuples. Each tuple will have three elements: (a, b, c) where 'a' is the total number of distinct integers of the type mentioned in the 'types' key, 'b' is the sum of those numbers, and 'c' is the sum of squares of those numbers. If there are no integers of the type mentioned in 'types' in the 'numbers' list, set the corresponding tuple to (0, 0, 0).
"""

def multi_dimensional_input(dict_lst):
    results = {'even': (0, 0, 0), 'odd': (0, 0, 0)}
    for data in dict_lst:
        numbers = data['numbers']
        number_type = data['types']
        if number_type == 'even':
            numbers = [num for num in numbers if num % 2 == 0]
        else:
            numbers = [num for num in numbers if num % 2 != 0]
        if numbers:
            a = len(set(numbers))
            b = sum(numbers)
            c = sum([i**2 for i in numbers])
            results[number_type] = (a, b, c)
    return results