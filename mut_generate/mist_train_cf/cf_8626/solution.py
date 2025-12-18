"""
QUESTION:
Define a function `print_nested` that recursively prints elements in a nested list or tuple without using a loop, stopping after a specified number of elements. The function should handle both lists and tuples, as well as nested structures with elements of different types. The function should include a counter to keep track of the number of elements printed and stop printing when the counter reaches the specified limit.
"""

def print_nested(nested, limit):
    def print_nested_helper(nested, limit, counter):
        if counter >= limit:
            return

        if isinstance(nested, (list, tuple)):
            for element in nested:
                print_nested_helper(element, limit, counter)
                counter += 1
                if counter >= limit:
                    return
        else:
            print(nested)
            counter += 1
    
    print_nested_helper(nested, limit, 0)