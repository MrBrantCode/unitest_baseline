"""
QUESTION:
Write a function named `find_path` that takes a multidimensional list (`md_list`) and an `element` as input. The function should return the path to the `element` in the multidimensional list as a list of indices. If the `element` is not found, the function should return `None`.
"""

def find_path(md_list, element):   
    def helper(sub_list, element, path):
        for i in range(len(sub_list)):
            if sub_list[i] == element:
                return path + [i]
            elif isinstance(sub_list[i], list):
                found_in_sublist = helper(sub_list[i], element, path + [i])
                if found_in_sublist:
                    return found_in_sublist
        return None

    return helper(md_list, element, [])