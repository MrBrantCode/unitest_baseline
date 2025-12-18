"""
QUESTION:
Return the result of evaluating a given boolean expression, represented as a string.
An expression can either be:

"t", evaluating to True;
"f", evaluating to False;
"!(expr)", evaluating to the logical NOT of the inner expression expr;
"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...

 
Example 1:
Input: expression = "!(f)"
Output: true

Example 2:
Input: expression = "|(f,t)"
Output: true

Example 3:
Input: expression = "&(t,f)"
Output: false

Example 4:
Input: expression = "|(&(t,f,t),!(t))"
Output: false

 
Constraints:

1 <= expression.length <= 20000
expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
expression is a valid expression representing a boolean, as given in the description.
"""

def evaluate_boolean_expression(expression: str) -> bool:
    def get_next_expr(expression, start):
        if expression[start] in {'!', '|', '&'}:
            open_count = 1
            close_count = 0
            start += 1
            while open_count > close_count:
                start += 1
                if expression[start] == '(':
                    open_count += 1
                if expression[start] == ')':
                    close_count += 1
            return start + 1
        else:
            return start + 1

    if expression == 'f':
        return False
    if expression == 't':
        return True
    if expression[0] == '!':
        return not evaluate_boolean_expression(expression[2:-1])
    if expression[0] == '|':
        cursor = 2
        while cursor < len(expression) - 1:
            end_of_next = get_next_expr(expression, cursor)
            if evaluate_boolean_expression(expression[cursor:end_of_next]):
                return True
            cursor = end_of_next + 1
        return False
    if expression[0] == '&':
        cursor = 2
        while cursor < len(expression) - 1:
            end_of_next = get_next_expr(expression, cursor)
            if not evaluate_boolean_expression(expression[cursor:end_of_next]):
                return False
            cursor = end_of_next + 1
        return True