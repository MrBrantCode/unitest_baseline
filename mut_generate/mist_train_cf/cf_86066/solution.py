"""
QUESTION:
Create a function named `distill_unique_elements` that takes a list `s` as input and returns a sequence of unique elements from the list in the order of their occurrence. Implement an auxiliary function `organize_elements` within `distill_unique_elements` to create a custom data structure that holds elements in the order of their occurrence without duplicates. The `organize_elements` function should take a list `e`, and two indices `index1` and `index2` as input. Do not use built-in data structures like sets or dictionaries with the `organize_elements` function.
"""

def distill_unique_elements(s: list):
    """
    Returns the elements in the list that do not repeat, in their order of occurrence.
    """
    def organize_elements(e: list, index1: int, index2: int):
        """
        Function to organize elements. This function will serve as an ordered set, 
        where we add elements in their order of occurrence, discarding duplicates.
        """
        base_list = e[index1:index2+1]
        return_list=[]
        for i in base_list: 
            if i not in return_list: 
                return_list.append(i)
        return return_list

    seen = organize_elements(s, 0, len(s)-1)
    for elem in seen:
        yield elem