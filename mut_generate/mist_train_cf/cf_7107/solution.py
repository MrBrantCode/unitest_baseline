"""
QUESTION:
Write a function `convert_number_to_string(num)` that takes an integer `num` as input and returns a string representation of the number. The function should satisfy the following conditions:
- The input number must be between 1000 and 999999 (inclusive).
- The output string should have each digit separated by a hyphen (-).
- The output string should be reversed.
- If the input number is not within the specified range, return an error message.
- The function should handle cases where the input number has leading zeros, trailing zeros, repeating digits, non-numeric characters, negative numbers, and floating-point numbers correctly.
- The time complexity of the function should be O(logn), where n is the number of digits in the input number.
- The space complexity of the function should be O(1), meaning it should not use additional data structures to store the converted string.
"""

def convert_number_to_string(num):
    if not isinstance(num, int) and not isinstance(num, float):
        return "Error: Input number must be numeric."
    if isinstance(num, float) or num < 1000 or num > 999999:
        return "Error: Input number must be between 1000 and 999999."
    
    num_str = str(int(num))  # Convert number to string and remove trailing zeros
    
    if num_str[0] == '-':
        num_str = num_str[1:]  # Remove the negative sign if present
    
    reversed_str = num_str[::-1]  # Reverse the string
    
    # Insert hyphens between each digit
    reversed_str = "-".join(reversed_str[i:i+1] for i in range(0, len(reversed_str)))
    
    return reversed_str