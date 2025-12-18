"""
QUESTION:
The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers. 

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

If the score < 0, return 0.

For example:
```
checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
```
"""

def calculate_exam_score(correct_answers, student_answers):
    """
    Calculate the score for a student's exam answers based on the correct answers.

    :param correct_answers: List of strings representing the correct answers.
    :param student_answers: List of strings representing the student's answers.
    :return: Integer representing the calculated score.
    """
    score = 0
    for correct, student in zip(correct_answers, student_answers):
        if student == "":
            continue
        elif student == correct:
            score += 4
        else:
            score -= 1
    return max(0, score)