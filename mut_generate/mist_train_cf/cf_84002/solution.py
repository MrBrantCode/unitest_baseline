"""
QUESTION:
Write a function `hash_sum(string, integers)` that takes a string of lowercase letters and a list of integers as input. The function should pair each character's hash value with the corresponding integer in the list and calculate the sum of these products. If the string and list are not the same length, return an error message. The function should also print the ASCII value of each character along with its corresponding integer.
"""

def hash_sum(string, integers):
    if len(string) != len(integers):
        return "Error: Lengths of string and list are not equal."

    total_sum = 0
    for i in range(len(string)):
        char = string[i]
        integer = integers[i]

        ASCII = ord(char)
        print("ASCII value of", char, "is", ASCII, "with respective integer", integer)

        total_sum += hash(char) * integer

    return total_sum