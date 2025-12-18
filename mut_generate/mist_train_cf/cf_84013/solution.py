"""
QUESTION:
Write a function `find_number(percentage)` that determines the original number and its reversed sequence of digits for a given percentage. The original number has n digits and its digit in the nth place is 4 less than seven times the digit in the (n-1)th place. The newly formed n-digit number, after reversing the digits in some order, is a certain percentage of the original number. The function should return the original number and its reversed sequence of digits, or None if no valid number is found.
"""

def find_number(percentage):
    n = 2
    a = 1
    b = 4

    while True:
        number = b * (10 ** (n - 1)) + a
        reversed_number = a * (10 ** (n - 1)) + b

        if reversed_number == (percentage / 100) * number:
            return number, "".join(str(number)[i] for i in reversed(range(len(str(number)))))

        n += 1
        a = b
        b = 7 * a - 4

        if n > 10 or b > 9:  
            return None, None