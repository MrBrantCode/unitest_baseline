"""
QUESTION:
Write a function `get_data_type_indices` that takes a list as input and returns a dictionary where the keys are the data types (either int or float) in the list and the values are lists containing the indices of the elements with that data type. The dictionary should be sorted in ascending order of the data types. The function should also return a dictionary with the count of each data type present in the list.
"""

def get_data_type_indices(my_list):
    data_types = [int, float]
    data_type_indices = {}
    data_type_count = {}
    
    for i, element in enumerate(my_list):
        if type(element) in data_types:
            if type(element) not in data_type_indices:
                data_type_indices[type(element)] = [i]
                data_type_count[type(element)] = 1
            else:
                data_type_indices[type(element)].append(i)
                data_type_count[type(element)] += 1
    
    sorted_data_type_indices = dict(sorted(data_type_indices.items(), key=lambda x: x[0].__name__))
    
    return sorted_data_type_indices, data_type_count