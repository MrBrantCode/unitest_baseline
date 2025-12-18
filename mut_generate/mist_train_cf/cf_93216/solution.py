"""
QUESTION:
Create a function called "calculate_correlation" that takes two numerical lists x and y of length n (1 <= n <= 10^6) as input and returns their correlation coefficient as a floating-point number rounded to 4 decimal places. The correlation coefficient should be calculated using the formula: (sum((xi - x_mean) * (yi - y_mean)) / (n * x_stddev * y_stddev)), where xi and yi are elements of x and y, x_mean and y_mean are their mean values, and x_stddev and y_stddev are their standard deviations. Do not use any built-in correlation functions or libraries.
"""

import math

def calculate_correlation(x, y):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    x_stddev = math.sqrt(sum((xi - x_mean)**2 for xi in x) / n)
    y_stddev = math.sqrt(sum((yi - y_mean)**2 for yi in y) / n)
    
    correlation = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (n * x_stddev * y_stddev)
    
    return round(correlation, 4)