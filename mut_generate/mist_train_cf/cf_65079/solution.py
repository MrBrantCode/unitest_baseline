"""
QUESTION:
Create a function `arrange_array` that takes an array of non-negative integers as input and returns the array sorted in ascending order based on the following rules:

* The primary key for sorting is the total number of zeros in the binary representation of each integer.
* In case of a tie, the secondary key for sorting is the divisibility by 2 of the zero count in the binary representation.
* If there is still a tie, the final sorting should be based on the decimal value of the integers.

The function should not include any error checking for non-integer or negative inputs, and it should assume that the input array only contains non-negative integers.
"""

def arrange_array(array):
    def number_of_zeros_in_binary(n):
        return bin(n).count('0') - 1  # subtract 1 because 'bin' adds a '0b' prefix

    def divisibility_of_zeros_by_two(n):
        return number_of_zeros_in_binary(n) % 2

    array.sort(key=lambda x: (number_of_zeros_in_binary(x), divisibility_of_zeros_by_two(x), x))
    return array