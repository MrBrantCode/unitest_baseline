"""
QUESTION:
Write a function `concatenate_strings` that takes a list of strings as input, and returns a new list where each element at index i is the concatenation of all other strings in the list except the string at index i. The input list will not be empty, and the solution should have a time complexity of O(n) where n is the length of the input list.
"""

def concatenate_strings(input_list):
    result = []
    total_len = sum(len(s) for s in input_list)
    for i in range(len(input_list)):
        concatenated = ""
        for j in range(len(input_list)):
            if i != j:
                concatenated += input_list[j]
        result.append(concatenated)
    return result