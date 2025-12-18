"""
QUESTION:
Create a function named `sort_strings` that takes two parameters: a list of strings and a dictionary defining a custom alphabetical order, where each key is a character and its corresponding value is a unique integer. The function should return the sorted list of strings based on the following rules:
- The product of the integer values of the characters in each string in ascending order.
- If two strings have the same product, they should be sorted by their length in descending order.
- If two strings have the same product and length, they should be sorted in reverse lexicographical order.
- If a string contains characters not present in the alphabetical order dictionary, consider their value as -1 for sorting purposes.
"""

def sort_strings(strings, alphabet_order):
    def get_product(string):
        product = 1
        for char in string:
            if char in alphabet_order:
                product *= alphabet_order[char]
            else:
                product *= -1
        return product

    return sorted(strings, key=lambda x: (get_product(x), -len(x), x[::-1]))