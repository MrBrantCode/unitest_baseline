"""
QUESTION:
Create a function `classify_student_grade` to classify a student's grade from A to D based on their final exam grade, assignment scores, and attendance record. The function should consider the final exam grade worth 60% of the total grade and the assignment scores worth 40%. The function should handle missing data for any of the inputs.
"""

def classify_student_grade(final_exam_grade=None, assignment_scores=None, attendance_record=None):
    """
    Classify a student's grade from A to D based on their final exam grade, assignment scores, and attendance record.

    Args:
    final_exam_grade (float): The student's final exam grade (default is None).
    assignment_scores (list): A list of the student's assignment scores (default is None).
    attendance_record (float): The student's attendance record (default is None).

    Returns:
    str: The student's grade (A, B, C, or D).
    """

    # Check if final exam grade is available
    if final_exam_grade is None:
        return 'D'

    # Check if final exam grade is >= 60%
    if final_exam_grade < 60:
        # Check if assignment scores are available
        if assignment_scores is not None:
            # Calculate average assignment score
            avg_assignment_score = sum(assignment_scores) / len(assignment_scores)
            # Check if average assignment score is >= 70%
            if avg_assignment_score >= 70:
                # Check if attendance record is available
                if attendance_record is not None:
                    # Check if attendance record is >= 75%
                    if attendance_record >= 75:
                        return 'B'
                    else:
                        return 'C'
                else:
                    return 'C'
            else:
                return 'D'
        else:
            return 'D'
    else:
        return 'A'