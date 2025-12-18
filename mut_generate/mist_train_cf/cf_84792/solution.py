"""
QUESTION:
Create a function `assign_grade(num_grade)` that takes a numerical grade as input, determines the corresponding letter grade with pluses and minuses (A+, A, A-, etc.), and handles non-numerical inputs and grades outside the 0-100 range by returning an error message.
"""

def assign_grade(num_grade):
    try:
        num_grade = float(num_grade)
        assert 0 <= num_grade <= 100
    except ValueError:
        return "Error: Grade must be a numerical value."
    except AssertionError:
        return "Error: Grade must be in the range 0 - 100."

    if num_grade >= 90:
        letter = 'A'
    elif num_grade >= 80:
        letter = 'B'
    elif num_grade >= 70:
        letter = 'C'
    elif num_grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    if letter != 'F':  
        if num_grade % 10 >= 7: 
            letter += '+'
        elif num_grade % 10 < 3:
            letter += '-'

    return letter