"""
QUESTION:
Write a function that finds the next number that is both pentagonal and hexagonal, starting from n = 144, given that every hexagonal number is also a triangular number. The function should use the formula for hexagonal numbers, H_n = n(2n - 1), and check if the generated hexagonal number is also pentagonal using the derived quadratic equation from the pentagonal formula.
"""

def entrance(n):
    def is_pentagonal(hexagonal):
        pentagonal_test = (1 + (24*hexagonal + 1)**0.5) / 6
        if pentagonal_test == int(pentagonal_test):
            return True
        else:
            return False

    while True:
        hexagonal = n*(2*n - 1)
        if is_pentagonal(hexagonal):
            return hexagonal
        n += 1