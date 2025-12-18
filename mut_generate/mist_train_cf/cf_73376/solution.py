"""
QUESTION:
Write a function `calculate_and_filter` that takes a list of integers as input. The function should calculate the product of all numbers in the list that satisfy the condition `x % 3 == 1`. It should also create a new list containing all numbers from the input list that satisfy the condition `x % 2 == 0` and return the sum of this new list, along with the calculated product.
"""

def calculate_and_filter(original_list):
    product = 1
    new_list = []
    
    # Iterate through the list
    for num in original_list:
        
        # Check if number matches first criterion,
        # if so, multiply it with the product.
        if num % 3 == 1:
            product *= num
        
        # Check if number matches second criterion,
        # if so, add it to new list.
        if num % 2 == 0:
            new_list.append(num)
            
    return product, sum(new_list)