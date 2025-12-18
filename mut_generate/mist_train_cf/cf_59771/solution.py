"""
QUESTION:
Create a function called `harmonic_mean(num1, num2, num3)` that calculates the harmonic mean of three numbers. The function should take three arguments, all of which must be non-zero, positive integers. If any of the inputs are not valid, the function should return an error message indicating that only positive, non-zero integers are allowed.
"""

def harmonic_mean(num1, num2, num3):
    if str(num1).isdigit() and str(num2).isdigit() and str(num3).isdigit() and int(num1) > 0 and int(num2) > 0 and int(num3) > 0:
        n1 = int(num1)
        n2 = int(num2)
        n3 = int(num3)
        return 3 / (1/n1 + 1/n2 + 1/n3)
    else:
        return "Invalid input. Please provide positive, non-zero integers only."