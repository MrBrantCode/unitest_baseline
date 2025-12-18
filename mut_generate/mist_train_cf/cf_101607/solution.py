"""
QUESTION:
The function 'pass_exam' takes an 'exam' object with attributes 'material' and 'weakness' as input. The 'pass_exam' function should return a string "pass" after simulating the process of preparing, practicing, reviewing the exam material, and taking the exam.
"""

def pass_exam(exam):
    prepare(exam.material)
    practice(exam)
    review(exam.material, exam.weakness)
    take_exam(exam)
    return "pass"