"""
QUESTION:
Create a function named `process_tuple` that accepts a tuple of numeric values. The function should display each value in the tuple, calculate the sum of the values, and calculate the average of the values. The function should handle any unexpected errors during execution and return the sum and average if successful, otherwise return `None` for both.
"""

def process_tuple(input_tuple):
    try:
        sum_tuple = 0
        count = 0
        for value in input_tuple:
            print("Value: ", value)
            sum_tuple += value
            count += 1
        avg_tuple = sum_tuple / count
    except TypeError as e:
        print("Type Error occurred: " + str(e))
        return None, None
    except ZeroDivisionError as e:
        print("Zero Division Error occurred: " + str(e))
        return None, None
    except Exception as e:
        print("An error occurred: " + str(e))
        return None, None

    return sum_tuple, avg_tuple