"""
QUESTION:
Develop a function named `find_largest` that takes three numbers (`num1`, `num2`, `num3`) as input and returns the largest of the three numbers.
"""

def find_largest(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else:
        return num3