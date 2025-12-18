"""
QUESTION:
Design a function `remove_tuples(t, condition)` that removes tuples from a given tuple `t` based on a provided condition. The condition is a function that accepts a tuple and returns a boolean. The function should handle nested tuples of arbitrary depth, preserve the sequence of the remaining elements, and handle exceptions that may be thrown by the condition function.
"""

def remove_tuples(t, condition):
    result = []
    for i in t:
        if isinstance(i, tuple):
            # recursively process nested tuple
            temp = remove_tuples(i, condition)
            try:
                # only retain the tuple if it doesn't meet condition
                if not temp or not condition(temp):
                    result.append(temp)
            except Exception as e:
                print(f"An exception occurred while evaluating the condition: {e}")
        else:
            result.append(i)
    return tuple(result)