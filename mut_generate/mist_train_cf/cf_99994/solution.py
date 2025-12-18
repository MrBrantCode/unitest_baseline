"""
QUESTION:
Create a function named `pass_exam` that takes an `exam` object as input and returns a string indicating whether the exam was passed or not. The `exam` object should have attributes `material` and `weakness`. The function should call four other functions: `prepare`, `practice`, `review`, and `take_exam`, in that order, using the `exam` object and its attributes as arguments.
"""

def pass_exam(exam):
    prepare(exam.material)
    practice(exam)
    review(exam.material, exam.weakness)
    take_exam(exam)
    return "pass"