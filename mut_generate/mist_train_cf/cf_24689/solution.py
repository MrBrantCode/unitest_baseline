"""
QUESTION:
Write a function `find_correlation_coefficient(x, y)` that calculates the correlation coefficient between two lists of numbers `x` and `y` of equal length. The function should return the correlation coefficient value. The lists contain at least two elements and all elements are numbers.
"""

def find_correlation_coefficient(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum([pow(x[i], 2) for i in range(n)])
    squared_sum_y = sum([pow(y[i], 2) for i in range(n)])
    product_sum = sum([x[i]*y[i] for i in range(n)])
    num = product_sum - (sum_x * sum_y/n)
    den = ((squared_sum_x - (pow(sum_x,2) / n)) * (squared_sum_y - (pow(sum_y,2) / n))) ** 0.5
    r = num/den
    return r