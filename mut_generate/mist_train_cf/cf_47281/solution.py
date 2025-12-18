"""
QUESTION:
Create a function `expunge_tuples` that takes two arguments: `complex_tuple` and `designated_tuple`. The function should remove all occurrences of `designated_tuple` from `complex_tuple`, including those nested within other tuples, while preserving the original sequence of the remaining elements. The function should compare tuples using the "==" operator.
"""

def expunge_tuples(complex_tuple, designated_tuple):
    # Recursive function to handle nested tuples
    def traverse_tuple(t):
        temp_list = []
        for i in t:
            # If i is a tuple
            if isinstance(i, tuple):
                # And if i is the designated_tuple
                if i == designated_tuple:
                    continue
                else:
                    temp_list.append(traverse_tuple(i))
            # Else, i is another type of element
            else:
                temp_list.append(i)
        return tuple(temp_list)

    result = traverse_tuple(complex_tuple)
    return result