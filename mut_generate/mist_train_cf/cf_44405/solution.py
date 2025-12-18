"""
QUESTION:
Write a function `optimised_scale(values, factor)` that takes a list of numbers `values` and a scaling `factor`, scales each number in the list by the factor, and returns the resulting list. The function should handle lists of varying sizes (from 5 to 1,000,000 elements) without significant performance impact. Implement effective error handling for potential issues such as memory overflow and type errors for incompatible input types.
"""

def optimised_scale(values, factor):
    result = []
    for value in values:
        try:
            result.append(value * factor)
        except TypeError as e:
            print("TypeError: ", e)
        except OverflowError as e:
            print("OverflowError: ", e)
        except MemoryError as e:
            print("MemoryError: ", e)
            break
    return result