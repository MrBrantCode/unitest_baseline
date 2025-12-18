"""
QUESTION:
Write a function `recursive_search` that takes four arguments: two numbers `num1` and `num2`, a list of numbers `numbers`, and a recursion limit. The function should multiply `num1` and `num2`, then search for the result in the `numbers` list. If the result is found, return it. If not, repeat the search up to the specified recursion limit. If the limit is reached without finding a match, return an error message.
"""

def recursive_search(num1, num2, numbers, limit):
    def multiply_and_search(num1, num2, numbers):
        result = num1 * num2
        if result in numbers:
            return result
        else:
            return None

    if limit == 0:
        return "Error: No match found within recursion limit."
    result = multiply_and_search(num1, num2, numbers)
    if result:
        return result
    else:
        return recursive_search(num1, num2, numbers, limit-1)