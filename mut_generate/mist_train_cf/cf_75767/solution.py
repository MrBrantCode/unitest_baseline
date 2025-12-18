"""
QUESTION:
Implement the function `advanced_sort(l: list, n: int, k: int)`. It takes a list `l` and two integers `n` and `k` as input, and returns a new list where elements at indices not divisible by `n` are the same as the original list, and elements at indices divisible by `n` are replaced with the same index element of the original list multiplied by `k`, then reversed.
"""

def advanced_sort(l: list, n: int, k: int):
    new_list = list()  # Create a new empty list
    target_indices = list()  # Placeholder for the indices to be targeted
    target_elements = list()  # Placeholder for the elements to be targeted

    # Identify the target indices and elements while filling up the new list
    for i in range(len(l)):
        if i % n == 0:
            target_indices.append(i)
            target_elements.append(l[i] * k)
            new_list.append(None)
        else:
            new_list.append(l[i])

    # Handle the second step
    for i in range(len(target_indices)):
        new_list[target_indices[i]] = target_elements[len(target_elements)-i-1]

    return new_list