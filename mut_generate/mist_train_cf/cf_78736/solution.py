"""
QUESTION:
Create a function called `delete_element` that takes in two parameters: a list (`lst`) and an index (`index`). This function should delete the element at the specified index from the list and return the updated list. 

The function should handle the following edge cases:
- If the input is not a list, return "Error: Input is not a list".
- If the list is empty, return "Error: List is empty".
- If the index is not in the range of the list (i.e., less than 0 or greater than or equal to the length of the list), return "Error: Index out of range".
"""

def delete_element(lst, index):
    if not isinstance(lst, list):
        return "Error: Input is not a list"
    
    if len(lst) == 0:
        return "Error: List is empty"
    
    if index < 0 or index >= len(lst):
        return "Error: Index out of range"
    
    del lst[index]
    
    return lst