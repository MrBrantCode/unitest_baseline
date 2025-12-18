"""
QUESTION:
Write a function `calc_microscopes` that takes three parameters: `springfield_num`, `increase_rate`, and `years`, where `springfield_num` is the current number of microscopes at Springfield Elementary School, `increase_rate` is the annual increase rate in percent, and `years` is the number of years to calculate the microscope count for. The function should return the number of microscopes at Shelbyville Elementary School after `years` years, rounded to the nearest integer, considering that Shelbyville's microscopes are initially 4/5 of Springfield's and increase by `increase_rate` percent every year.
"""

import math

def calc_microscopes(springfield_num, increase_rate, years):
    # Calculate the current number of microscopes at Shelbyville school
    shelbyville_num = springfield_num * 4/5
    
    # Calculate the increment over the given number of years
    for i in range(years):
        shelbyville_num *= (1 + increase_rate/100)
        
    # Return the result rounded to the nearest integer
    return math.floor(shelbyville_num + 0.5)