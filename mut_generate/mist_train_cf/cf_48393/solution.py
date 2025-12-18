"""
QUESTION:
Create a function named `multiply_from_binary_trees` that multiplies two integers, each represented as a binary tree where the in-order traversal of the tree provides the digit sequence of the integer. The function should take two lists of integers representing the in-order traversal of the binary trees as input, and return the product of the two integers.
"""

def multiply_from_binary_trees(entity1_data, entity2_data):
    # function to calculate the number
    def calculate_number(arr):
        num = 0
        for digit in arr:
            num = num*10 + digit
        return num

    entity1_num = calculate_number(entity1_data)
    entity2_num = calculate_number(entity2_data)

    return entity1_num * entity2_num