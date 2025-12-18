"""
QUESTION:
Find all possible sub-sequences of digits from a given list of numbers whose product equals a specified target number. The function should return a list of lists where each sublist contains the digits of a valid sub-sequence. The function should take two parameters: a list of numbers and a target number. The function should use recursion to explore all possible combinations of digits.
"""

def entrance(list_of_numbers, target):
    def make_combinations(index, product, selected_numbers):
        if index == len(list_of_numbers):
            if product == target:
                return [selected_numbers]
            else:
                return []
        else:
            # each time, we take a decision whether to include current element in the product or not.
            # Case 1. include current element.
            include_combinations = make_combinations(index+1, product*list_of_numbers[index], selected_numbers + [list_of_numbers[index]])
            # Case 2. don't include current element.
            exclude_combinations = make_combinations(index+1, product, selected_numbers)
            return include_combinations + exclude_combinations

    return make_combinations(0, 1, [])