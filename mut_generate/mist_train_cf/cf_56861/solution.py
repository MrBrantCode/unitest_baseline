"""
QUESTION:
Design an optimized function `datatype_sorter` that efficiently sorts a list of mixed datatype elements (integers, floats, and strings) in Python, considering memory usage and time complexity. The function should sort the elements of the same datatype in ascending order while maintaining their original order among different datatypes. It should also handle potential errors due to datatype misalignment.
"""

def datatype_sorter(input_list):
    int_list = []
    float_list = []
    string_list = []
    
    for i in input_list:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == float:
            float_list.append(i)
        elif type(i) == str:
            string_list.append(i)
            
    int_list.sort()
    float_list.sort()
    string_list.sort()
    
    return int_list + float_list + string_list