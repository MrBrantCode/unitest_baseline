"""
QUESTION:
Write a function `sequence_sum(start, end)` that calculates the series sum of all n^2-2n for a given range of n (start to end) without using any built-in functions. The function should be non-iterative and validate the inputs. The inputs start and end should be integers, greater than 0, and less than or equal to 99999. Additionally, start should be less than or equal to end.
"""

def sequence_sum(start, end):
    if type(start) is not int or start < 1 or start > 99999:
        return "Invalid input"
    if type(end) is not int or end < 1 or end > 99999:
        return "Invalid input"
    if start > end:
        return "Invalid input"

    def compute_term(n):
        return (n * n) - (2 * n)

    if start == end:
        return compute_term(start)
    else:
        return compute_term(start) + sequence_sum(start + 1, end)