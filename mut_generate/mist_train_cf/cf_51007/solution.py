"""
QUESTION:
Create a Python function `merge_tuples` that accepts three tuples `t1`, `t2`, and `t3` as input parameters. Using recursion, compare the lengths of the tuples and return an error message if they do not match. If the lengths are equal, merge the elements into a single list in the format [element of `t1`, element of `t2`, element of `t3`, ...]. Additionally, create a dictionary where the elements of `t1` are the keys and the corresponding elements of `t2` and `t3` are the values in a list. The function should not use any external libraries or built-in functions for merging or comparing tuples, except for the `len()` function to get the length of the tuples.
"""

def merge_tuples(t1, t2, t3):
    if len(t1) != len(t2) or len(t1) != len(t3):
        return "Error: Tuple lengths do not match!"
    
    def merge(i, result=[]):
        if i >= len(t1):
            return result
        else:
            return merge(i+1, result + [t1[i], t2[i], t3[i]])
    
    merged_list = merge(0)

    key_list = []
    val_list = []
    for i, item in enumerate(merged_list):
        if i % 3 == 0:
            key_list.append(item)
        else:
            val_list.append(item)

    return [merged_list, {key_list[i] : val_list[2*i:2*i+2] for i in range(len(key_list))}]