"""
QUESTION:
Create a function `stringShift` that takes in a string `s` and a 2D list `shift` where each inner list contains two integers, `direction` and `amount`. The function should return the resulting string after applying all shifts. The string `s` contains only lowercase English letters and has a length between 1 and 100. The `shift` list has a length between 1 and 100, and for each inner list, `direction` is either 0 (left shift) or 1 (right shift), and `amount` is between 0 and 100.
"""

def stringShift(s, shift):
    shift_total = sum(i*-1 if d==0 else i for d,i in shift)
    shift_total = shift_total % len(s)
    return s[-shift_total:] + s[:-shift_total]