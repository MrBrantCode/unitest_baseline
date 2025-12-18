"""
QUESTION:
Write a function called `divide_numbers` that takes two parameters, `numerator` and `denominator`, and returns the result of dividing the `numerator` by the `denominator`. Use a try-except-else-finally statement to handle the potential `ZeroDivisionError` that may occur when dividing by zero. If an exception occurs, print an error message. If no exception occurs, print a success message. The finally block should print a message indicating the end of the function execution.
"""

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print("An error occurred:", str(e))
    else:
        return result
    finally:
        print("This block always executes")