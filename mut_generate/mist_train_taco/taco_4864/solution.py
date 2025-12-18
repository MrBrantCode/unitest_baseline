"""
QUESTION:
Dr .: Peter, I've finally done it.

Peter: See you again? What kind of silly invention is this time?

Dr .: I finally came up with a revolutionary way to process mathematical formulas on a computer. Look at this table.

Ordinary notation | Dr.'s "breakthrough" notation
--- | ---
1 + 2 | 1 2 +
3 * 4 + 7 | 3 4 * 7 +
10 / (2 --12) | 10 2 12-/
(3-4) * (7 + 2 * 3) | 3 4 --7 2 3 * + *



Peter: Yeah.

Dr .: Fufufu. This alone won't tell you what it means to an inexperienced person. It's important from here.

Peter: I mean ...

Dr .: You know that computers have a data structure called a stack. Look, that's "first in, then out".

Peter: Yes. I know, that ...

Dr .: This groundbreaking notation uses that stack. For example, this 10 2 12-/, but process as follows.

Processing target | 10 | 2 | 12 |-| /
--- | --- | --- | --- | --- | ---
| ↓ | ↓ | ↓ | ↓ 2-12 | ↓ 10 / -10
Stack | |.
---
..
Ten
| ..
---
2
Ten
| 12
---
2
Ten
| ..
---
-Ten
Ten
| ..
---
..
-1



Dr .: How is it? You don't have to worry about parentheses or operator precedence, right? The word order is also "10 divided by 2 minus 12", which is somewhat similar to his Far Eastern island nation, Japanese. With this epoch-making invention, our laboratory is safe. Fafafa.

Peter: I mean, Doctor. I learned this in the basic course at the University of Aizu when I was in Japan. Everyone had a simple program called "Reverse Polish Notation".

Dr .: ...

So, instead of Peter, I decided to teach this program to the doctor. Create a program that inputs the formula written in "Reverse Polish Notation" and outputs the calculation result.



input

Given multiple datasets. For each dataset, a formula in Reverse Polish Notation (a string of up to 80 characters with integers and arithmetic symbols separated by one blank character (half-width)) is given on one line. No formula is given that divides a value by 0 or a value that is as close to 0 as possible.

The number of datasets does not exceed 50.

output

Output the calculation result (real number) on one line for each data set. The calculation result may include an error of 0.00001 or less.

Example

Input

10 2 12 - /
3 4 - 7 2 3 * + *
-1 -2 3 + +


Output

-1.000000
-13.000000
0.000000
"""

def evaluate_rpn(expression: str) -> float:
    """
    Evaluates a mathematical expression given in Reverse Polish Notation (RPN).

    Parameters:
    expression (str): A string representing the RPN expression.

    Returns:
    float: The result of the RPN expression, with a precision of up to 6 decimal places.
    """
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            c = str(eval(a + token + b))
            stack.append(c)
        else:
            stack.append(token)
    
    return float(stack[0])