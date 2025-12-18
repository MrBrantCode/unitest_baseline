"""
QUESTION:
Create a function named `multiply` that takes two lists of integers `lst1` and `lst2` as input. For each list, calculate the product of the elements at even indices that are odd and the sum of the elements that are even. Return a tuple containing the two products and two sums.
"""

def multiply(lst1, lst2):
    # Initialize variables to hold products and sums
    product1, product2, sum1, sum2 = 1, 1, 0, 0

    # Iterate through lst1
    for i in range(len(lst1)):
        # Check if index is even and element is odd
        if i % 2 == 0 and lst1[i] % 2 != 0:
            product1 *= lst1[i]
        # Check if element is even for adding to sum
        if lst1[i] % 2 == 0:
            sum1 += lst1[i]

    # Iterate through lst2
    for i in range(len(lst2)):
        # Check if index is even and element is odd
        if i % 2 == 0 and lst2[i] % 2 != 0:
            product2 *= lst2[i]
        # Check if element is even for adding to sum
        if lst2[i] % 2 == 0:
            sum2 += lst2[i]

    # Return the two products and two sum values
    return (product1, product2, sum1, sum2)