"""
QUESTION:
Create a function named `pass_exam` that takes an `exam` object as a parameter, where the `exam` object contains attributes for the exam's material and areas of weakness. The function should simulate the process of passing an exam by preparing for the exam material, practicing the exam, reviewing the material and areas of weakness, and taking the exam. The function should return the string "pass". The exam object should have methods for preparing for the material, practicing the exam, reviewing the material and areas of weakness, and taking the exam.
"""

def pass_exam(exam):
    prepare(exam.material)
    practice(exam)
    review(exam.material, exam.weakness)
    take_exam(exam)
    return "pass"