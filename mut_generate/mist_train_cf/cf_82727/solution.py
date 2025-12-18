"""
QUESTION:
Create a function `find_mode(numbers)` that takes a list of numbers as input and returns the number that appears most frequently in the list, assuming there is only one mode. The function should have a time complexity of O(n), where n is the size of the input list.
"""

def find_mode(numbers):
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    max_count = max(count_dict.values())
    mode = [k for k, v in count_dict.items() if v == max_count]
    
    return mode[0]