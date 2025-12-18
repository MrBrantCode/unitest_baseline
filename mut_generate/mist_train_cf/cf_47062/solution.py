"""
QUESTION:
Develop a function called `merge_sort_string_list` that iteratively performs a merge sort on a list of strings. The function should take two parameters: `string_list` (the list of strings to be sorted) and `reverse` (an optional boolean parameter that defaults to `False`, indicating whether the list should be sorted in lexicographical or reverse lexicographical order). The function should handle lists of any size, including empty lists, and should be able to handle duplicate strings.
"""

def merge_sort_string_list(string_list, reverse=False):
    if len(string_list) <= 1:
        return string_list

    def merge(left, right):
        result = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if reverse:
                if right[right_index] <= left[left_index]:
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1
            else:
                if left[left_index] <= right[right_index]:
                    result.append(left[left_index])
                    left_index += 1
                else:
                    result.append(right[right_index])
                    right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result

    midpoint = len(string_list) // 2
    left_half = merge_sort_string_list(string_list[:midpoint], reverse)
    right_half = merge_sort_string_list(string_list[midpoint:], reverse)

    return merge(left_half, right_half)