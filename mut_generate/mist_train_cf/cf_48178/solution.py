"""
QUESTION:
Create a function named `find_unpaired` that takes a list of unique integers as input and returns a new list containing all unpaired elements. An unpaired element is defined as a number that appears only once in the list. The function should have a time complexity of O(N) for efficiency.
"""

def find_unpaired(my_list):
    count_dict = {}
    for num in my_list:
        count_dict[num] = count_dict.get(num, 0) + 1
        
    return [key for key, value in count_dict.items() if value == 1]