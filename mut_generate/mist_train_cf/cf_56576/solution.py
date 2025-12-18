"""
QUESTION:
Insert a given number into a list with mixed ascending and descending sequences while maintaining the existing orders. The list may contain multiple ascending and descending sequences. The number should be inserted at the correct position to maintain the order of the sequences. 

The function should take two parameters: a list of integers and an integer value to be inserted. The function should return the modified list with the value inserted at the correct position. 

Example input: List = [1, 3, 5, 8, 10, 15, 7, 2], value = 6.
"""

def entrance(List, value):
    inverted = False 
    for i in range(len(List) - 1):
        if inverted == False: 
            if List[i] < value and List[i + 1] >= value: 
                List.insert(i + 1, value)
                return List
            if List[i] > List[i + 1]: 
                inverted = True
        else: 
            if List[i] > value and List[i + 1] <= value: 
                List.insert(i + 1, value)
                return List
    List.append(value) 
    return List