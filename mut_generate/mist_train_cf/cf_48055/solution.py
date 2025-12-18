"""
QUESTION:
Write a function `grade_converter(rating)` that takes a numerical rating between 1 and 100 and returns its corresponding academic grading equivalent. The function should validate the input rating and return "Invalid rating" if it's not within the interval 1 and 100, both inclusive. The mapping between numerical rating and symbolic grades is as follows:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60
Use a functional programming approach with if, else-if, and else statements, and include at least three different comparison operators.
"""

def grade_converter(rating):
    if rating < 1 or rating > 100:
        return 'Invalid rating'
    elif rating >= 90:
        return 'A'
    elif rating >= 80:
        return 'B'
    elif rating >= 70:
        return 'C'
    elif rating >= 60:
        return 'D'
    else:
        return 'F'