"""
QUESTION:
Create a function named `sort_mixed_list` that takes a list of mixed variable types as input, including integers, floating point numbers, and strings. The function should sort the strings alphabetically, the integers in descending order, and the floating point numbers in ascending order. The function must keep each type in their original place in the list.
"""

def sort_mixed_list(m_list):
    #Seperate list by types
    str_list = sorted([i for i in m_list if type(i) == str])
    int_list = sorted([i for i in m_list if type(i) == int], reverse=True)
    float_list = sorted([i for i in m_list if type(i) == float])
    
    # Start to sort
    for idx, elem in enumerate(m_list):
        if type(elem) == str:
            m_list[idx] = str_list.pop(0)
        elif type(elem) == int:
            m_list[idx] = int_list.pop(0)
        elif type(elem) == float:
            m_list[idx] = float_list.pop(0)
            
    return m_list