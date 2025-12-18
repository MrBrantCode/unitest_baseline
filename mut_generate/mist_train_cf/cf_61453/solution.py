"""
QUESTION:
Develop a function called `student_info` that takes two parameters: `marks` and `scores`, where `marks` is the scored marks of a student in a single discipline, and `scores` is a list of scores of other students in the same discipline. The function should return the academic grade of the student based on the scored marks and their percentile rank among the given set of scores. 

The grades should be determined using the following pattern: 
- 90-100: A+,
- 80-89: A,
- 70-79: B,
- 60-69: C,
- below 60: Fail.

The percentile should be calculated as the percentage of scores below the given marks, inclusive. Ensure that the function includes conditions to handle corner cases, such as when the input contains non-numerical values or when the scored marks are not in the list of other scores.
"""

from bisect import bisect_right

def student_info(marks, scores):
    """
    This function returns the grade and percentile of a student, based on the marks scored and the scores of other students.
    :param marks: int, mark scored by the student
    :param scores: list, scores of other students
    :return: str, grade and percentile of the student
    """
    if not all(isinstance(x, (int, float)) for x in [marks]+scores): 
        return "Error: All inputs should be numeric values."
    if marks < 0 or marks > 100:
        return "Error: Scored marks not within valid range."
    scores.sort()
    index = bisect_right(scores, marks)
    percentile = 100.0 * index / len(scores)
    if marks < 60:
        grade = 'Fail'
    elif 60 <= marks < 70:
        grade = 'C'
    elif 70 <= marks < 80:
        grade = 'B'
    elif 80 <= marks < 90:
        grade = 'A'
    elif 90 <= marks <= 100:
        grade = 'A+'
    else:
        return 'Invalid marks'
    return "Grade: {}, Percentile: {:.2f}%".format(grade, percentile)