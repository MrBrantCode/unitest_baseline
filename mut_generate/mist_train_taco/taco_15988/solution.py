"""
QUESTION:
View Russian Translation

One day Benny decides to miss lessons. But as she is a very good pig she will do her homework anyway. She doesn't know anything about the content of this lessons. Your task is to help her.

The problem is following: you are given a right triangle with coordinates of vertices (0, 0), (0, a), (b, 0) and integer p. You may choose any value val and draw a vertical line x = val. After that let area(val) be the area of the part of triangle at the right side of this line. Your task is to find such minimal val that area(val) is not more than p% of the area of the given triangle.

Input

The first and the only one line contains three integers a, b and p.

Output

Output in a single line answer to the problem with two signs after decimal point.

It is guaranteed that the answer+10^-6 and answer-10^-6 would produce the same rounded answer.

Constraints
1 ≤ a, b ≤ 10^7
1 ≤ p < 100
1 ≤ a, b ≤ 10^3 holds for test cases worth 20% of the problem's score.

SAMPLE INPUT
2 2 25

SAMPLE OUTPUT
1.00
"""

import math

def find_minimal_val(a: int, b: int, p: int) -> float:
    """
    Finds the minimal value 'val' such that the area to the right of the line x = val
    is not more than p% of the area of the given right triangle with vertices (0, 0), (0, a), (b, 0).

    Parameters:
    a (int): The y-coordinate of the triangle's vertex.
    b (int): The x-coordinate of the triangle's vertex.
    p (int): The percentage of the triangle's area.

    Returns:
    float: The minimal 'val' rounded to two decimal places.
    """
    p = p / 100.0  # Convert percentage to a fraction
    required_area = 0.5 * a * b * p  # Calculate the required area
    result = b - math.sqrt(2 * required_area * b / a)  # Calculate the minimal 'val'
    return round(result, 2)  # Round the result to two decimal places