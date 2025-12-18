"""
QUESTION:
Implement a function named `str_to_int_list_advanced` that takes a string of comma-separated and newline-separated integers, grouped by parentheses. The string is expected to be in the format of "(int,int,...)\n(int,int,...)\n...", where each line represents a group of integers. The function should return a list of lists where each sublist corresponds to each line of integer groups from the string. If the input string contains any non-integer values or the string does not conform to the required format, the function should raise a warning message for each non-conforming line.
"""

def str_to_int_list_advanced(my_str):
    lines = my_str.split('\n')
    res = []
    for idx, line in enumerate(lines, start=1):
        line = line.strip()
        if not line.startswith('(') or not line.endswith(')'):
            print(f"Warning: Input at line {idx} does not conform to format")
            continue
        try:
            numbers = [int(num) for num in line[1:-1].split(',')]
        except ValueError:
            print(f"Warning: Input at line {idx} does not conform to format")
            continue
        res.append(numbers)
    return res