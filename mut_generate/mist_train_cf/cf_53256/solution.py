"""
QUESTION:
Develop a function named `unique_orderings` that generates a specified number of unique re-orderings of a provided numerical list considering two conditions: 
- The even numbers in the array must stay in their original indices.
- If the given array contains duplicate values, treat them as distinct for reordering purposes but consider them the same when applying the first condition.
 
The function should take two parameters: 
- `number`: The specified number of unique re-orderings to be generated.
- `array`: The provided numerical list.

The function should return an error if it's impossible to generate the requested number of reorderings due to insufficient possible unique permutations.
"""

import itertools

def unique_orderings(number, array):
    # get the number of permutations
    count = len(list(itertools.permutations(array)))

    # check if it's impossible to generate the requested number of reorderings
    if count < number:
        return 'Error: Insufficient possible unique permutations!'

    # get the indices of even numbers
    even_indices = [i for i, x in enumerate(array) if x % 2 == 0]

    combinations = list(itertools.permutations(array, len(array)))
    unique_combinations = []

    for combination in combinations:
        # check if the even numbers are at their original indices
        if all(combination[i]==array[i] for i in even_indices):
            unique_combinations.append(combination)
            if len(unique_combinations) == number:
                break

    return [list(c) for c in unique_combinations]