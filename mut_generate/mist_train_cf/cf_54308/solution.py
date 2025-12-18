"""
QUESTION:
Write a function named `parse_nested_parens_and_validate` that takes a string containing multiple groups of nested parentheses separated by spaces as input. The function should return a list of integers representing the maximum depth of each valid group of parentheses. If any group is invalid (i.e., not properly nested), the function should raise an exception.
"""

def parse_nested_parens_and_validate(s: str) -> list:
    """
    This function takes a string containing multiple groups of nested parentheses 
    separated by spaces as input, and returns a list of integers representing 
    the maximum depth of each valid group of parentheses.

    Args:
        s (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        list: A list of integers representing the maximum depth of each valid group of parentheses.

    Raises:
        Exception: If any group is invalid (i.e., not properly nested).
    """

    def is_valid(group: str) -> bool:
        """Helper function to check if a group of parentheses is valid."""
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    groups = s.split()
    depths = []
    for group in groups:
        if not is_valid(group):
            raise Exception('Invalid group of parentheses in input string: ' + group)
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif char == ')':
                depth -= 1
        depths.append(max_depth)
    return depths