"""
QUESTION:
Write a function `get_grade(score)` that assigns a grade to a student based on their score. The function should return "D" if the score is higher than 80, lower than 90, and a prime number, and "F" otherwise. The input score will be a positive integer less than or equal to 10^9, and the function should run within a time complexity of O(sqrt(N)), where N is the input score.
"""

import math

def get_grade(score):
    if 80 < score < 90:
        for i in range(2, int(math.sqrt(score)) + 1):
            if score % i == 0:
                return "F"
        return "D"
    else:
        return "F"