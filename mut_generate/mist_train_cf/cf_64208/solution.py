"""
QUESTION:
Create a Python function named `custom_function` that takes two string parameters, `greeting` and `random_str`. This function should return a string containing `greeting` concatenated with the reversed version of `random_str`. Additionally, the function must print the length of the resulting string without using any built-in `reverse` or `length` functions. The solution should utilize recursive functions and string manipulation.
"""

def custom_function(greeting, random_str):
    def get_length(input_str):
        if input_str == '':
            return 0
        else:
            return 1 + get_length(input_str[1:])

    def reverse_string(input_str):
        if input_str == '':
            return input_str
        else:
            return reverse_string(input_str[1:]) + input_str[0]

    reversed_string = reverse_string(random_str)
    final_output = greeting + " " + reversed_string
    len_final_output = get_length(final_output)
    print("Length of the final output: ", len_final_output)
    return final_output