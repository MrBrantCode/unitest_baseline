"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a set of unique integers. The function should handle lists containing elements of different data types, including strings that may represent integers. If a string cannot be converted to an integer, it should be skipped and an error message should be printed. All numbers in the input list should be converted to integers before being added to the set.
"""

def remove_duplicates(input_list):
    output_list = set()
    for i in input_list:
        if isinstance(i, (int, float)):  
            output_list.add(int(i))  
        elif isinstance(i, str):  
            try:
                output_list.add(int(i))  
            except ValueError:
                print(f"Invalid integer value: {i}")
                continue  
    return output_list