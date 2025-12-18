"""
QUESTION:
Create a function `sorted_based_on_parity_and_magnitude` that takes a list of non-negative integers as input and returns the sorted list based on the following rules:
- The count of ones in their binary representation in ascending order
- Their magnitude in descending order
- If there are ties, use the parity of the count of ones (even or odd) to break the tie, with even counts first
- If there are still ties, use the decimal value for sorting
The function should include a custom comparator function to achieve the desired sorting order.
"""

def sorted_based_on_parity_and_magnitude(arr):
    def bit_count(n):
        return bin(n).count('1')

    arr.sort(key=lambda x: (bit_count(x)%2, bit_count(x), -x))

    return arr