"""
QUESTION:
Write a function called `generate_unique_permutations` that takes a string as input and returns all unique permutations of the input string without using any built-in permutation functions or recursion. The input string can be up to 10 characters long and may contain alphanumeric characters and duplicates.
"""

def generate_unique_permutations(string):
    result = [[]]
    for character_index in range(len(string)):
        temporary = []
        for partial_result in result:
            for character_position in range(len(partial_result) + 1):
                copy_partial_result = list(partial_result)
                copy_partial_result.insert(character_position, string[character_index])
                temporary.append(copy_partial_result)
        result = temporary

    final_result = []
    for each_result in result:
        perm = ''.join(each_result)
        if perm not in final_result: 
            final_result.append(perm)
    return final_result