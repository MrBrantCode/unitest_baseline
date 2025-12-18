"""
QUESTION:
Write a function `find_multiples(multiples, start, end)` that takes in a list of integers `multiples`, and two numerical values `start` and `end`, which can be provided as strings or other non-integer types. The function should return a list of unique multiples of the provided integers that lie within the range of `start` and `end` (inclusive), as well as the sum of these multiples calculated manually without using built-in sum functions. If the inputs cannot be converted to integers, the function should return an error message.
"""

def find_multiples(multiples, start, end):
    # Convert string or other non-integer inputs to integers
    try:
        multiples = [int(x) for x in multiples]
        start = int(start)
        end = int(end)
    except Exception:
        return "Invalid inputs. Please provide integers only."

    # Initialize list for multiples and sum variable
    multiples_list = set()
    multiples_sum = 0

    # Find multiples in range
    for num in range(start, end+1):
        for m in multiples:
            if num % m == 0 and num not in multiples_list:
                multiples_list.add(num)
                # Add unique multiples to the sum
                multiples_sum += num

    # Return sum and list of multiples
    return list(multiples_list), multiples_sum