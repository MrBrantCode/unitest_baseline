"""
QUESTION:
Implement a function `shift_zeros` that takes a list `arr` as input and rearranges its elements such that all occurrences of zero (including "0" and "0.0") are moved to the end of the list while maintaining the relative order of non-zero elements. The function should handle multiple levels of nested lists and refrain from using pre-existing Python functions or libraries that directly solve the problem. The function should also be efficient in handling large lists, ensuring a time complexity of O(n), where n is the total number of elements in the main list and all nested lists.
"""

def shift_zeros(arr):
    def helper(arr, non_zeros, zeros):
        for item in arr:
            if type(item) is list:
                non_zeros, zeros = helper(item, non_zeros, zeros)
            elif item in [0, "0", "0.0"]:
                zeros.append(item)
            else:
                non_zeros.append(item)
        return non_zeros, zeros

    non_zeros, zeros = helper(arr, [], [])
    return non_zeros + zeros