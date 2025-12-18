"""
QUESTION:
Write a function called `array_product` that takes a 2D array of integers as input and returns a tuple containing the product of all non-zero elements in the array and a list of the product of non-zero elements in each sub-array. If any sub-array is empty, return the message "An empty sub-array was found in the array."
"""

def array_product(arr):
    all_product = 1
    row_products = []
    
    for sublist in arr:
        if sublist:
            row_product = 1
            for elem in sublist:
                if elem != 0:
                    row_product *= elem
                    all_product *= elem
            row_products.append(row_product)
        else:
            return "An empty sub-array was found in the array."
    
    return all_product, row_products