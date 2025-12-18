"""
QUESTION:
Develop a function `pythagorean_quadruplet` that accepts an integer `y` and returns the smallest Pythagorean quadruplet (a, b, c, d) with a sum equal to `y`. The function should cater for negative integer values of `y`, returning "No solution" if it's impossible to find a Pythagorean quadruplet with the given sum. Optimize the function to perform efficiently on large inputs of `y` and apply memoization if necessary.
"""

def pythagorean_quadruplet(y):
    if y < 0:
        return "No solution"
    for a in range(1, y//4 + 1):
        for b in range(a, (y - a)//3 + 1):
            c = (y - a - b - 1)//2
            d = y - a - b - c
            if a*a + b*b + c*c == d*d and a<=b<=c<=d:
                return a, b, c, d
    return "No solution"