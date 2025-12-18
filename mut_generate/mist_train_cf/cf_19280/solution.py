"""
QUESTION:
Write a function `multiply_list_recursive` that takes a list of integers and returns a new list with the same values multiplied by 5. The function should have a time complexity of O(n), where n is the length of the input list, and should be able to handle lists with up to 10^6 elements without using any built-in functions or libraries. The input list will only contain positive integers, and the order of duplicates in the input list should be maintained in the output list.
"""

def multiply_list_recursive(input_list):
    """
    This function takes a list of integers and returns a new list with the same values multiplied by 5.
    
    The function has a time complexity of O(n), where n is the length of the input list, 
    and can handle lists with up to 10^6 elements without using any built-in functions or libraries.
    
    The input list will only contain positive integers, and the order of duplicates in the input list 
    is maintained in the output list.
    
    :param input_list: A list of integers
    :return: A new list with the same values multiplied by 5
    """
    def helper(input_list, output_list, index):
        # Base case: if index reaches the end of the list
        if index == len(input_list):
            return output_list
        
        # Multiply the current value by 5 and append it to the output list
        output_list.append(input_list[index] * 5)
        
        # Recursive call with incremented index
        return helper(input_list, output_list, index + 1)

    return helper(input_list, [], 0)