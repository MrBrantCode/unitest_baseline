"""
QUESTION:
Implement a function `subsets` that generates all possible subsets of 7 unique elements from an input numeric array in ascending order. The function should also handle an optional input `sum_threshold` and return only subsets where the sum of the subset elements is greater than `sum_threshold`. If `sum_threshold` is not provided, the function should return all subsets. The input array will have at least 7 unique integers ranging from -1000 to 1000. The function should not use any built-in combinations method.
"""

def subsets(input_list, sum_threshold=None):
    input_list.sort()
    result = []

    def recursive(index, subset):
        if len(subset) == 7:
            if sum_threshold is None or sum(subset) > sum_threshold:
                result.append(subset)
            return

        if index == len(input_list):
            return

        recursive(index + 1, subset + [input_list[index]])
        recursive(index + 1, subset)

    recursive(0, [])
    return result