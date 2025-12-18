"""
QUESTION:
Write a recursive function `generate_balanced_parentheses(n, left_count, right_count, digits)` to generate all possible combinations of balanced parentheses given a certain number of pairs `n`, where each pair of parentheses must have at least one digit between them, and the digits within each pair of parentheses must be in strictly ascending order. The function should use `left_count` and `right_count` to keep track of the number of left and right parentheses, and `digits` to store the formed combination.
"""

def generate_balanced_parentheses(n, left_count, right_count, digits):
    if left_count == 0 and right_count == 0:
        print(digits)
        return
    
    if left_count > 0:
        generate_balanced_parentheses(n, left_count - 1, right_count, digits + "(")
    
    if right_count > left_count:
        generate_balanced_parentheses(n, left_count, right_count - 1, digits + ")")
    
    if n > 0:
        for i in range(1, n+1):
            if digits and digits[-1].isdigit():
                if int(digits[-1]) < i:
                    generate_balanced_parentheses(n-1, left_count, right_count, digits + str(i) + "(" + str(i) + ")")
            else:
                generate_balanced_parentheses(n-1, left_count, right_count, digits + str(i) + "(" + str(i) + ")")