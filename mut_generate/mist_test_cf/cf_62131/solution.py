"""
QUESTION:
Write a function complex_sum that takes a list of strings as input. Each string contains only digits. The function should return a list where the i-th item indicates the quantity of odd elements within the i-th string from input. Replace all instances of 'i's with the actual frequency of odd numericals in the output string. The function should handle faulty inputs like non-string elements within the list or strings that contain non-numeric values by returning "ERROR".
"""

def complex_sum(lst):
    """In the context of a list solely composed of string objects encapsulating digits, deliver a list. 
    The i-th item of the response should indicate "the quantity of odd elements within the i'th string from input." while substituting all the 'i's with the actual frequency of odd numericals. 
    For an extra test, ascertain the function nicely manages faulty inputs like non-string elements incorporated within the list, or strings that contain elements that are not numeric values.
    """
    response = []

    for item in lst:
        if not isinstance(item, str):
            return "ERROR"

        odd_number_count = 0
        for char in item:
            if not char.isdigit():
                return "ERROR"
            if int(char) % 2 != 0:
                odd_number_count += 1

        result_string = "the quantity of odd components {}n the str{}ng {} of the {}nput.".format(odd_number_count, odd_number_count, odd_number_count, odd_number_count)
        response.append(result_string)

    return response