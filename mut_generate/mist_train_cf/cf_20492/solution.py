"""
QUESTION:
Create a function called `merge_and_sort_lists` that takes two lists as arguments and returns a new list containing the elements from both input lists, with no duplicates, in descending order, without using any built-in list functions or methods like `append()` or `extend()`.
"""

def merge_and_sort_lists(list_1, list_2):
    def remove_duplicates(lst):
        unique_list = []
        for element in lst:
            if element not in unique_list:
                unique_list += [element]
        return unique_list

    def sort_descending(lst):
        for i in range(len(lst)):
            max_idx = i
            for j in range(i+1, len(lst)):
                if lst[j] > lst[max_idx]:
                    max_idx = j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
        return lst

    new_list = list_1 + list_2
    new_list = remove_duplicates(new_list)
    return sort_descending(new_list)