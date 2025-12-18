"""
QUESTION:
Create a function called `count_upper` that determines the total number of unique uppercase letters in a given string and returns a dictionary with the count of each individual uppercase letter. The function should be able to handle both normal strings and binary strings, as well as non-string inputs. If the input is not a string, the function should return an error message.
"""

def count_upper(test_str):
    if isinstance(test_str, str):
        result_dict = {}
        binary_chars = {'0', '1'}
        
        # Check if the string is binary
        if set(test_str) <= binary_chars:
            # Convert to regular string if binary
            test_str = ''.join(chr(int(test_str[i:i+8], 2)) for i in range(0, len(test_str), 8))
        for char in test_str:
            if char.isupper():
                if char in result_dict:
                    result_dict[char] += 1
                else:
                    result_dict[char] = 1
        return len(result_dict), result_dict
    else:
        return "Error: Input must be a type of string"